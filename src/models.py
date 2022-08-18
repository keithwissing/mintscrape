from typing import List, Optional, Any

from pydantic import BaseModel

# class Addresses(BaseModel):
#     realEstateStatus: str
#     address1: str

class OlderAccount(BaseModel):
    linkedAccountId: Any
    accountName: str
    addAccountDate: int
    fiLoginDisplayName: str
    ccAggrStatus: Optional[int]
    exclusionType: str
    linkedAccount: Any
    isHiddenFromPlanningTrends: bool
    isTerminal: bool
    linkCreationTime: Any
    isActive: bool
    accountStatus: str
    accountSystemStatus: str
    lastUpdated: int
    fiLastUpdated: int
    yodleeAccountNumberLast4: Optional[str]
    isError: bool
    fiName: str
    isAccountNotFound: bool
    klass: str
    possibleLinkAccounts: List
    lastUpdatedInString: str
    accountTypeInt: int
    currency: str
    id: int
    isHostAccount: bool
    value: float
    fiLoginId: int
    usageType: Optional[str]
    interestRate: Optional[float]
    accountType: str
    currentBalance: float
    fiLoginStatus: str
    isAccountClosedByMint: bool
    userName: Optional[str]
    yodleeName: str
    closeDate: Optional[int]
    linkStatus: str
    accountId: int
    isClosed: bool
    fiLoginUIStatus: str
    yodleeAccountId: Optional[int]
    name: str
    status: str
    dueDate: Optional[str] = None
    dueAmt: Optional[float] = None
    rateType: Optional[int] = None
    origAmount: Optional[Optional[float]] = None
    origDate: Optional[str] = None
    rate: Optional[Optional[float]] = None
    term: Optional[int] = None
    amountDue: Optional[Optional[float]] = None
    # addresses: Optional[Addresses] = None
    isValueUserDefined: Optional[bool] = None
    provider: Optional[str] = None
    useKBB: Optional[bool] = None

class ModelItem(BaseModel):
    type: str
    bankAccountType: Optional[str] = None
    availableBalance: Optional[float] = None
    interestRate: Optional[float] = None
    cpInterestRate: Optional[float] = None
    minimumNoFeeBalance: Optional[float] = None
    userMinimumNoFeeBalance: Optional[float] = None
    monthlyFee: Optional[float] = None
    userMonthlyFee: Optional[float] = None
    userFreeBillPay: Optional[bool] = None
    userAtmFeeReimbursement: Optional[bool] = None
    numOfTransactions: Optional[float] = None
    id: str
    name: str
    value: float
    isVisible: bool
    isDeleted: bool
    planningTrendsVisible: bool
    accountStatus: str
    systemStatus: str
    currency: str
    fiLoginId: str
    fiLoginStatus: str
    currentBalance: float
    cpId: Optional[str] = None
    cpAccountName: str
    hostAccount: bool
    fiName: str
    accountTypeInt: int
    isAccountClosedByMint: bool
    isAccountNotFound: bool
    isActive: bool
    isClosed: bool
    isError: bool
    isHiddenFromPlanningTrends: bool
    isTerminal: bool
    createdDate: str
    lastUpdatedDate: str
    userCardType: Optional[str] = None
    creditAccountType: Optional[str] = None
    creditLimit: Optional[float] = None
    availableCredit: Optional[float] = None
    userRewardsType: Optional[str] = None
    rewardsRate: Optional[float] = None
    annualFee: Optional[float] = None
    minPayment: Optional[float] = None
    absoluteMinPayment: Optional[float] = None
    statementMinPayment: Optional[float] = None
    statementDueDate: Optional[str] = None
    statementDueAmount: Optional[float] = None
    cpAccountNumberLast4: Optional[str] = None
    credentialSetId: Optional[str] = None
    ccAggrStatus: Optional[str] = None
    investmentType: Optional[str] = None
    dormant401K: Optional[bool] = None
    totalUnvestedBalance: Optional[float] = None
    cashBalance: Optional[float] = None
    loanType: Optional[str] = None
    loanTermType: Optional[str] = None
    loanInterestRateType: Optional[str] = None
    originalLoanAmount: Optional[float] = None
    principalBalance: Optional[float] = None
    originationDate: Optional[str] = None
    realEstateType: Optional[str] = None
    realEstateTypeDesc: Optional[str] = None
    realEstateValueProviderType: Optional[str] = None
    accountDescription: Optional[str] = None
    providerValue: Optional[float] = None
    propertyType: Optional[str] = None
    userAddress: Optional[str] = None
    userZip: Optional[str] = None
    cyberHomesCity: Optional[str] = None
    cyberHomesState: Optional[str] = None
    cyberHomesZip: Optional[str] = None
    amountDue: Optional[float] = None
    vehicleType: Optional[str] = None
    vehicleTypeDesc: Optional[str] = None
    vehicleDetails: Optional[str] = None
    mileage: Optional[int] = None
    vehiclevalue: Optional[float] = None
    vehicleYear: Optional[int] = None
    makeId: Optional[int] = None
    modelId: Optional[int] = None
    isNew: Optional[bool] = None
    userEdited: Optional[bool] = None
    userValue: Optional[str] = None
    vehicleMake: Optional[str] = None
    vehicleModel: Optional[str] = None
    vehicleTrim: Optional[str] = None
    vehicleTrimID: Optional[str] = None
    kbbValueType: Optional[str] = None
    usageType: Optional[str] = None
