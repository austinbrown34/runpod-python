"""
RunPod | API Wrapper | Queries | Accounts
"""

QUERY_MYSELF = """
query myself {
  myself {
    id
    authId
    email
    currentSpendPerHr
    machineQuota
    referralEarned
    signedTermsOfService
    spendLimit
    stripeSavedPaymentId
    stripeSavedPaymentLast4
    templateEarned
    multiFactorEnabled
    underBalance
    minBalance
    stripeAutoReloadAmount
    stripeAutoPaymentThreshold
    clientBalance
    hostBalance
    hostStripeLinked
    stripeAccountId
    pubKey
    notifyPodsStale
    notifyPodsGeneral
    notifyLowBalance
    creditAlertThreshold
    notifyOther
    maxServerlessConcurrency
  }
}
"""
