import sgqlc.types


craft_api_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

String = sgqlc.types.String

ID = sgqlc.types.ID

Int = sgqlc.types.Int

Float = sgqlc.types.Float


########################################################################
# Input Objects
########################################################################

########################################################################
# Output Objects and Interfaces
########################################################################
class Query(sgqlc.types.Type):
    __schema__ = craft_api_schema
    company = sgqlc.types.Field('Company', graphql_name='company', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('duns', sgqlc.types.Arg(String, graphql_name='duns', default=None)),
        ('name_contains', sgqlc.types.Arg(String, graphql_name='nameContains', default=None)),
        ('domain', sgqlc.types.Arg(String, graphql_name='domain', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=Int(10))),
))
    )


class Company(sgqlc.types.Type):
    __schema__ = craft_api_schema
    acquisitions = sgqlc.types.Field(sgqlc.types.list_of('Acquisition'), graphql_name='acquisitions')
    balance_sheets = sgqlc.types.Field(sgqlc.types.list_of('BalanceSheet'), graphql_name='balanceSheets')
    balance_sheets_sources = sgqlc.types.Field(sgqlc.types.list_of('Source'), graphql_name='balanceSheetsSources')
    blog = sgqlc.types.Field(String, graphql_name='blog')
    cash_flow_statements = sgqlc.types.Field(sgqlc.types.list_of('CashFlowStatement'), graphql_name='cashFlowStatements')
    cash_flow_statements_sources = sgqlc.types.Field(sgqlc.types.list_of('Source'), graphql_name='cashFlowStatementsSources')
    company_ratings = sgqlc.types.Field('CompanyRatings', graphql_name='companyRatings')
    competitors = sgqlc.types.Field(sgqlc.types.list_of('Competitor'), graphql_name='competitors')
    country_of_registration = sgqlc.types.Field(String, graphql_name='countryOfRegistration')
    craft_url = sgqlc.types.Field(String, graphql_name='craftUrl')
    crunchbase = sgqlc.types.Field(String, graphql_name='crunchbase')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    duns = sgqlc.types.Field(String, graphql_name='duns')
    employees = sgqlc.types.Field(sgqlc.types.list_of('EmployeeNumber'), graphql_name='employees')
    ethnicity_metrics = sgqlc.types.Field(sgqlc.types.list_of('HumanCapitalMetric'), graphql_name='ethnicityMetrics')
    ev = sgqlc.types.Field('Money', graphql_name='ev')
    facebook = sgqlc.types.Field(String, graphql_name='facebook')
    facebook_likes = sgqlc.types.Field(sgqlc.types.list_of('SocialNetworkData'), graphql_name='facebookLikes')
    filings = sgqlc.types.Field(sgqlc.types.list_of('Filing'), graphql_name='filings')
    founded_year = sgqlc.types.Field(String, graphql_name='foundedYear')
    funding_rounds = sgqlc.types.Field(sgqlc.types.list_of('FundingRound'), graphql_name='fundingRounds')
    gender_metrics = sgqlc.types.Field(sgqlc.types.list_of('HumanCapitalMetric'), graphql_name='genderMetrics')
    glassdoor = sgqlc.types.Field(String, graphql_name='glassdoor')
    homepage = sgqlc.types.Field(String, graphql_name='homepage')
    id = sgqlc.types.Field(ID, graphql_name='id')
    income_statements = sgqlc.types.Field(sgqlc.types.list_of('IncomeStatement'), graphql_name='incomeStatements')
    income_statements_sources = sgqlc.types.Field(sgqlc.types.list_of('Source'), graphql_name='incomeStatementsSources')
    instagram = sgqlc.types.Field(String, graphql_name='instagram')
    job_categories = sgqlc.types.Field(sgqlc.types.list_of('JobCategory'), graphql_name='jobCategories')
    jobs = sgqlc.types.Field(sgqlc.types.list_of('Job'), graphql_name='jobs', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('per_page', sgqlc.types.Arg(Int, graphql_name='perPage', default=Int(50))),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    jobs_count = sgqlc.types.Field(Int, graphql_name='jobsCount')
    key_executives = sgqlc.types.Field(sgqlc.types.list_of('KeyExecutive'), graphql_name='keyExecutives')
    latest_share_price = sgqlc.types.Field('SharePrice', graphql_name='latestSharePrice')
    latest_zscore = sgqlc.types.Field('LatestZScore', graphql_name='latestZScore')
    linkedin = sgqlc.types.Field(String, graphql_name='linkedin')
    locations = sgqlc.types.Field(sgqlc.types.list_of('Location'), graphql_name='locations')
    locations_count = sgqlc.types.Field(Int, graphql_name='locationsCount')
    logo = sgqlc.types.Field('Image', graphql_name='logo')
    long_description = sgqlc.types.Field(String, graphql_name='longDescription')
    news = sgqlc.types.Field(sgqlc.types.list_of('NewsArticle'), graphql_name='news')
    operating_metrics = sgqlc.types.Field(sgqlc.types.list_of('OperatingMetric'), graphql_name='operatingMetrics')
    operating_metrics_sources = sgqlc.types.Field(sgqlc.types.list_of('Source'), graphql_name='operatingMetricsSources')
    pinterest = sgqlc.types.Field(String, graphql_name='pinterest')
    ratios = sgqlc.types.Field(sgqlc.types.list_of('Ratios'), graphql_name='ratios')
    revenue_breakdowns = sgqlc.types.Field(sgqlc.types.list_of('RevenueBreakdown'), graphql_name='revenueBreakdowns')
    roles_metrics = sgqlc.types.Field(sgqlc.types.list_of('HumanCapitalMetric'), graphql_name='rolesMetrics')
    salaries = sgqlc.types.Field(sgqlc.types.list_of('Salary'), graphql_name='salaries')
    short_description = sgqlc.types.Field(String, graphql_name='shortDescription')
    stocks_summary = sgqlc.types.Field('StocksSummary', graphql_name='stocksSummary')
    tags = sgqlc.types.Field(sgqlc.types.list_of('Tag'), graphql_name='tags')
    total_funding = sgqlc.types.Field('Money', graphql_name='totalFunding')
    twitter = sgqlc.types.Field(String, graphql_name='twitter')
    twitter_followers = sgqlc.types.Field(sgqlc.types.list_of('SocialNetworkData'), graphql_name='twitterFollowers')
    valuation = sgqlc.types.Field('Money', graphql_name='valuation')
    website_traffic = sgqlc.types.Field('WebsiteTraffic', graphql_name='websiteTraffic')
    wikipedia = sgqlc.types.Field(String, graphql_name='wikipedia')
    youtube = sgqlc.types.Field(String, graphql_name='youtube')


class Image(sgqlc.types.Type):
    __schema__ = craft_api_schema
    url = sgqlc.types.Field(String, graphql_name='url')


class Tag(sgqlc.types.Type):
    __schema__ = craft_api_schema
    name = sgqlc.types.Field(String, graphql_name='name')


class EmployeeNumber(sgqlc.types.Type):
    __schema__ = craft_api_schema
    date = sgqlc.types.Field(String, graphql_name='date')
    employee_growth = sgqlc.types.Field(Float, graphql_name='employeeGrowth')
    employee_number = sgqlc.types.Field(Int, graphql_name='employeeNumber')


class KeyExecutive(sgqlc.types.Type):
    __schema__ = craft_api_schema
    facebook = sgqlc.types.Field(String, graphql_name='facebook')
    headshot = sgqlc.types.Field('ExecutiveImageUrl', graphql_name='headshot')
    headshot_url = sgqlc.types.Field(String, graphql_name='headshotUrl')
    linkedin = sgqlc.types.Field(String, graphql_name='linkedin')
    name = sgqlc.types.Field(String, graphql_name='name')
    title = sgqlc.types.Field(String, graphql_name='title')
    twitter = sgqlc.types.Field(String, graphql_name='twitter')


class ExecutiveImageUrl(sgqlc.types.Type):
    __schema__ = craft_api_schema
    url = sgqlc.types.Field(String, graphql_name='url')


class Location(sgqlc.types.Type):
    __schema__ = craft_api_schema
    address = sgqlc.types.Field(String, graphql_name='address')
    city = sgqlc.types.Field(String, graphql_name='city')
    country = sgqlc.types.Field(String, graphql_name='country')
    hq = sgqlc.types.Field(Boolean, graphql_name='hq')
    latitude = sgqlc.types.Field(Float, graphql_name='latitude')
    longitude = sgqlc.types.Field(Float, graphql_name='longitude')
    state = sgqlc.types.Field(String, graphql_name='state')
    zip_code = sgqlc.types.Field(String, graphql_name='zipCode')


class Job(sgqlc.types.Type):
    __schema__ = craft_api_schema
    description = sgqlc.types.Field(String, graphql_name='description')
    job_title = sgqlc.types.Field(String, graphql_name='jobTitle')
    last_updated = sgqlc.types.Field(String, graphql_name='lastUpdated')
    location = sgqlc.types.Field(String, graphql_name='location')
    team_function = sgqlc.types.Field(String, graphql_name='teamFunction')


class JobCategory(sgqlc.types.Type):
    __schema__ = craft_api_schema
    category = sgqlc.types.Field(String, graphql_name='category')
    percentage = sgqlc.types.Field(Float, graphql_name='percentage')


class Money(sgqlc.types.Type):
    __schema__ = craft_api_schema
    amount = sgqlc.types.Field(Int, graphql_name='amount')
    currency = sgqlc.types.Field(String, graphql_name='currency')


class FundingRound(sgqlc.types.Type):
    __schema__ = craft_api_schema
    amount = sgqlc.types.Field(Money, graphql_name='amount')
    date = sgqlc.types.Field(String, graphql_name='date')
    investors = sgqlc.types.Field(sgqlc.types.list_of('Investor'), graphql_name='investors')
    share_price = sgqlc.types.Field(Float, graphql_name='sharePrice')
    shares_issued = sgqlc.types.Field(Int, graphql_name='sharesIssued')
    stage = sgqlc.types.Field(String, graphql_name='stage')
    total_shares_outstanding = sgqlc.types.Field(Int, graphql_name='totalSharesOutstanding')


class Investor(sgqlc.types.Type):
    __schema__ = craft_api_schema
    name = sgqlc.types.Field(String, graphql_name='name')


class SharePrice(sgqlc.types.Type):
    __schema__ = craft_api_schema
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    currency = sgqlc.types.Field(String, graphql_name='currency')
    date = sgqlc.types.Field(String, graphql_name='date')


class IncomeStatement(sgqlc.types.Type):
    __schema__ = craft_api_schema
    cost_of_goods_sold = sgqlc.types.Field(Float, graphql_name='costOfGoodsSold')
    currency = sgqlc.types.Field(String, graphql_name='currency')
    depreciation_amortization = sgqlc.types.Field(Float, graphql_name='depreciationAmortization')
    ebit = sgqlc.types.Field(Float, graphql_name='ebit')
    ebitda = sgqlc.types.Field(Float, graphql_name='ebitda')
    general_administrative_expense = sgqlc.types.Field(Float, graphql_name='generalAdministrativeExpense')
    gross_profit = sgqlc.types.Field(Float, graphql_name='grossProfit')
    interest_expense = sgqlc.types.Field(Float, graphql_name='interestExpense')
    interest_income = sgqlc.types.Field(Float, graphql_name='interestIncome')
    investment_income = sgqlc.types.Field(Float, graphql_name='investmentIncome')
    net_income = sgqlc.types.Field(Float, graphql_name='netIncome')
    period = sgqlc.types.Field('Period', graphql_name='period')
    pre_tax_profit = sgqlc.types.Field(Float, graphql_name='preTaxProfit')
    research_development_expense = sgqlc.types.Field(Float, graphql_name='researchDevelopmentExpense')
    revenue = sgqlc.types.Field(Float, graphql_name='revenue')
    sales_marketing_expense = sgqlc.types.Field(Float, graphql_name='salesMarketingExpense')
    total_operating_expense = sgqlc.types.Field(Float, graphql_name='totalOperatingExpense')


class Period(sgqlc.types.Type):
    __schema__ = craft_api_schema
    end_date = sgqlc.types.Field(String, graphql_name='endDate')
    period_type = sgqlc.types.Field(String, graphql_name='periodType')
    start_date = sgqlc.types.Field(String, graphql_name='startDate')


class Source(sgqlc.types.Type):
    __schema__ = craft_api_schema
    label = sgqlc.types.Field(String, graphql_name='label')
    url = sgqlc.types.Field(String, graphql_name='url')


class BalanceSheet(sgqlc.types.Type):
    __schema__ = craft_api_schema
    accounts_payable = sgqlc.types.Field(Float, graphql_name='accountsPayable')
    accounts_receivable = sgqlc.types.Field(Float, graphql_name='accountsReceivable')
    additional_paid_in_capital = sgqlc.types.Field(Float, graphql_name='additionalPaidInCapital')
    cash = sgqlc.types.Field(Float, graphql_name='cash')
    common_stock = sgqlc.types.Field(Float, graphql_name='commonStock')
    currency = sgqlc.types.Field(String, graphql_name='currency')
    current_assets = sgqlc.types.Field(Float, graphql_name='currentAssets')
    current_liabilities = sgqlc.types.Field(Float, graphql_name='currentLiabilities')
    dividends_payable = sgqlc.types.Field(Float, graphql_name='dividendsPayable')
    goodwill = sgqlc.types.Field(Float, graphql_name='goodwill')
    inventories = sgqlc.types.Field(Float, graphql_name='inventories')
    non_current_liabilities = sgqlc.types.Field(Float, graphql_name='nonCurrentLiabilities')
    period = sgqlc.types.Field(Period, graphql_name='period')
    pp_e = sgqlc.types.Field(Float, graphql_name='ppE')
    preferred_stock = sgqlc.types.Field(Float, graphql_name='preferredStock')
    retained_earnings = sgqlc.types.Field(Float, graphql_name='retainedEarnings')
    total_assets = sgqlc.types.Field(Float, graphql_name='totalAssets')
    total_equity = sgqlc.types.Field(Float, graphql_name='totalEquity')
    total_liabilities = sgqlc.types.Field(Float, graphql_name='totalLiabilities')


class CashFlowStatement(sgqlc.types.Type):
    __schema__ = craft_api_schema
    accounts_payable = sgqlc.types.Field(Float, graphql_name='accountsPayable')
    accounts_receivable = sgqlc.types.Field(Float, graphql_name='accountsReceivable')
    capex = sgqlc.types.Field(Float, graphql_name='capex')
    cash_from_financing_activities = sgqlc.types.Field(Float, graphql_name='cashFromFinancingActivities')
    cash_from_investing_activities = sgqlc.types.Field(Float, graphql_name='cashFromInvestingActivities')
    cash_from_operating_activities = sgqlc.types.Field(Float, graphql_name='cashFromOperatingActivities')
    currency = sgqlc.types.Field(String, graphql_name='currency')
    dividends_paid = sgqlc.types.Field(Float, graphql_name='dividendsPaid')
    free_cash_flow = sgqlc.types.Field(Float, graphql_name='freeCashFlow')
    income_taxes_paid = sgqlc.types.Field(Float, graphql_name='incomeTaxesPaid')
    interest_paid = sgqlc.types.Field(Float, graphql_name='interestPaid')
    inventories = sgqlc.types.Field(Float, graphql_name='inventories')
    net_income = sgqlc.types.Field(Float, graphql_name='netIncome')
    period = sgqlc.types.Field(Period, graphql_name='period')
    purchases_ppe = sgqlc.types.Field(Float, graphql_name='purchasesPpe')


class LatestZScore(sgqlc.types.Type):
    __schema__ = craft_api_schema
    period = sgqlc.types.Field(Period, graphql_name='period')
    value = sgqlc.types.Field(Float, graphql_name='value')


class Ratios(sgqlc.types.Type):
    __schema__ = craft_api_schema
    avg_days_inventory_out = sgqlc.types.Field(Float, graphql_name='avgDaysInventoryOut')
    avg_days_payable_out = sgqlc.types.Field(Float, graphql_name='avgDaysPayableOut')
    current_ratio = sgqlc.types.Field(Float, graphql_name='currentRatio')
    debt_to_assets_ratio = sgqlc.types.Field(Float, graphql_name='debtToAssetsRatio')
    debt_to_equity_ratio = sgqlc.types.Field(Float, graphql_name='debtToEquityRatio')
    ebit_interest_exp = sgqlc.types.Field(Float, graphql_name='ebitInterestExp')
    ebit_margin = sgqlc.types.Field(Float, graphql_name='ebitMargin')
    ebitda_capex_interest_exp = sgqlc.types.Field(Float, graphql_name='ebitdaCapexInterestExp')
    ebitda_interest_exp = sgqlc.types.Field(Float, graphql_name='ebitdaInterestExp')
    ebitda_margin = sgqlc.types.Field(Float, graphql_name='ebitdaMargin')
    ev_cfo = sgqlc.types.Field(Float, graphql_name='evCfo')
    ev_ebit = sgqlc.types.Field(Float, graphql_name='evEbit')
    ev_ebitda = sgqlc.types.Field(Float, graphql_name='evEbitda')
    ev_fcf = sgqlc.types.Field(Float, graphql_name='evFcf')
    financial_leverage = sgqlc.types.Field(Float, graphql_name='financialLeverage')
    fixed_asset_turnover = sgqlc.types.Field(Float, graphql_name='fixedAssetTurnover')
    gross_margin = sgqlc.types.Field(Float, graphql_name='grossMargin')
    inventory_turnover = sgqlc.types.Field(Float, graphql_name='inventoryTurnover')
    last_year = sgqlc.types.Field(String, graphql_name='lastYear')
    lt_debt_capital = sgqlc.types.Field(Float, graphql_name='ltDebtCapital')
    lt_debt_equity = sgqlc.types.Field(Float, graphql_name='ltDebtEquity')
    net_debt_ebitda = sgqlc.types.Field(Float, graphql_name='netDebtEbitda')
    net_debt_ebitda_capex = sgqlc.types.Field(Float, graphql_name='netDebtEbitdaCapex')
    net_income_margin = sgqlc.types.Field(Float, graphql_name='netIncomeMargin')
    operating_cash_flow_ratio = sgqlc.types.Field(Float, graphql_name='operatingCashFlowRatio')
    p_e = sgqlc.types.Field(Float, graphql_name='pE')
    period = sgqlc.types.Field(Period, graphql_name='period')
    quick_ratio = sgqlc.types.Field(Float, graphql_name='quickRatio')
    return_on_assets = sgqlc.types.Field(Float, graphql_name='returnOnAssets')
    return_on_capital = sgqlc.types.Field(Float, graphql_name='returnOnCapital')
    return_on_equity = sgqlc.types.Field(Float, graphql_name='returnOnEquity')
    revenue_per_employee = sgqlc.types.Field(Float, graphql_name='revenuePerEmployee')
    sgna_margin = sgqlc.types.Field(Float, graphql_name='sgnaMargin')
    total_asset_turnover = sgqlc.types.Field(Float, graphql_name='totalAssetTurnover')
    total_debt_capital = sgqlc.types.Field(Float, graphql_name='totalDebtCapital')
    total_debt_ebitda = sgqlc.types.Field(Float, graphql_name='totalDebtEbitda')
    total_debt_ebitda_capex = sgqlc.types.Field(Float, graphql_name='totalDebtEbitdaCapex')
    total_debt_equity = sgqlc.types.Field(Float, graphql_name='totalDebtEquity')
    total_liabilities_total_assets = sgqlc.types.Field(Float, graphql_name='totalLiabilitiesTotalAssets')
    z = sgqlc.types.Field(Float, graphql_name='z')
    z_double_prime = sgqlc.types.Field(Float, graphql_name='zDoublePrime')
    z_prime = sgqlc.types.Field(Float, graphql_name='zPrime')


class StocksSummary(sgqlc.types.Type):
    __schema__ = craft_api_schema
    beta = sgqlc.types.Field(Float, graphql_name='beta')
    consensus_eps = sgqlc.types.Field(Float, graphql_name='consensusEps')
    date = sgqlc.types.Field(String, graphql_name='date')
    day200_moving_avg = sgqlc.types.Field(Float, graphql_name='day200MovingAvg')
    day50_moving_avg = sgqlc.types.Field(Float, graphql_name='day50MovingAvg')
    day5_change_percent = sgqlc.types.Field(Float, graphql_name='day5ChangePercent')
    dividend_rate = sgqlc.types.Field(Float, graphql_name='dividendRate')
    dividend_yield = sgqlc.types.Field(Float, graphql_name='dividendYield')
    eps_surprise_dollar = sgqlc.types.Field(Float, graphql_name='epsSurpriseDollar')
    eps_surprise_percent = sgqlc.types.Field(Float, graphql_name='epsSurprisePercent')
    ex_dividend_date = sgqlc.types.Field(String, graphql_name='exDividendDate')
    insider_percent = sgqlc.types.Field(Float, graphql_name='insiderPercent')
    institution_percent = sgqlc.types.Field(Float, graphql_name='institutionPercent')
    latest_eps = sgqlc.types.Field(Float, graphql_name='latestEps')
    latest_eps_date = sgqlc.types.Field(String, graphql_name='latestEpsDate')
    marketcap = sgqlc.types.Field(Float, graphql_name='marketcap')
    month1_change_percent = sgqlc.types.Field(Float, graphql_name='month1ChangePercent')
    month3_change_percent = sgqlc.types.Field(Float, graphql_name='month3ChangePercent')
    month6_change_percent = sgqlc.types.Field(Float, graphql_name='month6ChangePercent')
    number_of_estimates = sgqlc.types.Field(Float, graphql_name='numberOfEstimates')
    pe_ratio_high = sgqlc.types.Field(Float, graphql_name='peRatioHigh')
    pe_ratio_low = sgqlc.types.Field(Float, graphql_name='peRatioLow')
    shares_outstanding = sgqlc.types.Field(Float, graphql_name='sharesOutstanding')
    short_date = sgqlc.types.Field(String, graphql_name='shortDate')
    short_interest = sgqlc.types.Field(Float, graphql_name='shortInterest')
    short_ratio = sgqlc.types.Field(Float, graphql_name='shortRatio')
    week52_change = sgqlc.types.Field(Float, graphql_name='week52Change')
    week52_high = sgqlc.types.Field(Float, graphql_name='week52High')
    week52_low = sgqlc.types.Field(Float, graphql_name='week52Low')
    year1_change_percent = sgqlc.types.Field(Float, graphql_name='year1ChangePercent')
    year2_change_percent = sgqlc.types.Field(Float, graphql_name='year2ChangePercent')
    year5_change_percent = sgqlc.types.Field(Float, graphql_name='year5ChangePercent')
    ytd_change_percent = sgqlc.types.Field(Float, graphql_name='ytdChangePercent')


class Filing(sgqlc.types.Type):
    __schema__ = craft_api_schema
    craft_url = sgqlc.types.Field(String, graphql_name='craftUrl')
    period = sgqlc.types.Field(Period, graphql_name='period')
    sec_url = sgqlc.types.Field(String, graphql_name='secUrl')


class Acquisition(sgqlc.types.Type):
    __schema__ = craft_api_schema
    date = sgqlc.types.Field(String, graphql_name='date')
    description = sgqlc.types.Field(String, graphql_name='description')
    duns = sgqlc.types.Field(String, graphql_name='duns')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    value = sgqlc.types.Field(Money, graphql_name='value')


class OperatingMetric(sgqlc.types.Type):
    __schema__ = craft_api_schema
    company_specific_kpi = sgqlc.types.Field(String, graphql_name='companySpecificKpi')
    footnotes = sgqlc.types.Field(String, graphql_name='footnotes')
    source = sgqlc.types.Field(Source, graphql_name='source')
    time_period = sgqlc.types.Field(Period, graphql_name='timePeriod')
    unit_type = sgqlc.types.Field(String, graphql_name='unitType')
    value = sgqlc.types.Field(Money, graphql_name='value')


class HumanCapitalMetric(sgqlc.types.Type):
    __schema__ = craft_api_schema
    name = sgqlc.types.Field(String, graphql_name='name')
    time_period = sgqlc.types.Field(Period, graphql_name='timePeriod')
    unit_type = sgqlc.types.Field(String, graphql_name='unitType')
    value = sgqlc.types.Field(Int, graphql_name='value')


class Salary(sgqlc.types.Type):
    __schema__ = craft_api_schema
    job_category = sgqlc.types.Field(String, graphql_name='jobCategory')
    median_salary = sgqlc.types.Field(Money, graphql_name='medianSalary')


class SocialNetworkData(sgqlc.types.Type):
    __schema__ = craft_api_schema
    amount = sgqlc.types.Field(Int, graphql_name='amount')
    date = sgqlc.types.Field(String, graphql_name='date')


class NewsArticle(sgqlc.types.Type):
    __schema__ = craft_api_schema
    headline = sgqlc.types.Field(String, graphql_name='headline')
    published_at = sgqlc.types.Field(String, graphql_name='publishedAt')
    source = sgqlc.types.Field(String, graphql_name='source')
    summary = sgqlc.types.Field(String, graphql_name='summary')
    url = sgqlc.types.Field(String, graphql_name='url')


class Competitor(sgqlc.types.Type):
    __schema__ = craft_api_schema
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    id = sgqlc.types.Field(ID, graphql_name='id')
    logo = sgqlc.types.Field(Image, graphql_name='logo')
    short_description = sgqlc.types.Field(String, graphql_name='shortDescription')


class RevenueBreakdown(sgqlc.types.Type):
    __schema__ = craft_api_schema
    period = sgqlc.types.Field(Period, graphql_name='period')
    values = sgqlc.types.Field(sgqlc.types.list_of('RevenueBreakdownPoint'), graphql_name='values')


class RevenueBreakdownPoint(sgqlc.types.Type):
    __schema__ = craft_api_schema
    segment_category = sgqlc.types.Field(String, graphql_name='segmentCategory')
    segment_name = sgqlc.types.Field(String, graphql_name='segmentName')
    segment_value = sgqlc.types.Field(String, graphql_name='segmentValue')
    unit_type = sgqlc.types.Field(String, graphql_name='unitType')


class CompanyRatings(sgqlc.types.Type):
    __schema__ = craft_api_schema
    career_opportunities_rating = sgqlc.types.Field(Float, graphql_name='careerOpportunitiesRating')
    compensation_and_benefits_rating = sgqlc.types.Field(Float, graphql_name='compensationAndBenefitsRating')
    culture_and_values_rating = sgqlc.types.Field(Float, graphql_name='cultureAndValuesRating')
    overall_rating = sgqlc.types.Field(Float, graphql_name='overallRating')
    senior_leadership_rating = sgqlc.types.Field(Float, graphql_name='seniorLeadershipRating')
    work_life_balance_rating = sgqlc.types.Field(Float, graphql_name='workLifeBalanceRating')


class WebsiteTraffic(sgqlc.types.Type):
    __schema__ = craft_api_schema
    company_url = sgqlc.types.Field(String, graphql_name='companyUrl')
    website_traffic_history = sgqlc.types.Field(sgqlc.types.list_of('WebsiteTrafficHistoryPoint'), graphql_name='websiteTrafficHistory')


class WebsiteTrafficHistoryPoint(sgqlc.types.Type):
    __schema__ = craft_api_schema
    date = sgqlc.types.Field(String, graphql_name='date')
    value = sgqlc.types.Field(Int, graphql_name='value')



########################################################################
# Unions
########################################################################
