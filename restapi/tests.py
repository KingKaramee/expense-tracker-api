## TEST DDT
from django.test import TestCase
from restapi import models

# Create your tests here.
class Testmodels(TestCase):
    def test_expense(self):
        expense = models.Expense.objects.create(
            amount=100,
            merchant="amazon",
            description="anc headphones",
            category="music",
        )
        inserted_expense = models.Expense.objects.get(pk=expense.id)

        self.assertEqual(100, inserted_expense.amount)
        self.assertEqual("amazon", inserted_expense.merchant)
        self.assertEqual("anc headphones", inserted_expense.description)
        self.assertEqual("music", inserted_expense.category)
