from rest_framework.routers import DefaultRouter

from v1 import viewsets

router = DefaultRouter()

router.register(
    r"bank-account",
    viewsets.BankAccountViewSet,
    basename="BankAccountViewSet",
)
router.register(
    r"business",
    viewsets.BusinessViewSet,
    basename="BusinessViewSet",
)
router.register(
    r"category",
    viewsets.CategoryViewSet,
    basename="CategoryViewSet",
)
router.register(
    r"recurring-transaction",
    viewsets.RecurringTransactionViewSet,
    basename="RecurringTransactionViewSet",
)
router.register(
    r"tax-consultant",
    viewsets.TaxConsultantViewSet,
    basename="TaxConsultantViewSet",
)
router.register(
    r"transaction",
    viewsets.TransactionViewSet,
    basename="TransactionViewSet",
)

app_name = "v1"
urlpatterns = router.urls
