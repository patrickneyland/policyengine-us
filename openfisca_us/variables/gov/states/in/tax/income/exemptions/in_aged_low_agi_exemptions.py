from openfisca_us.model_api import *


class in_base_exemptions(Variable):
    value_type = float
    entity = TaxUnit
    label = "IN base exemptions"
    unit = USD
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states["in"].tax.income.exemptions
        filing_status = tax_unit("filing_status", period)
        threshold = p.aged_low_agi.threshold[filing_status]
        aged_low_agi_exemption = p.aged_low_agi.amount
        agi = tax_unit("agi", period)
        age_threshold = parameters(period).gov.irs.deductions.standard.aged_or_blind.age_threshold
        aged_head = (
            tax_unit("age_head", period) >= age_threshold
            ) * 1
        aged_spouse = (
            tax_unit("age_spouse", period) >= age_threshold
            ) * 1
        income_eligible = where(agi < threshold, 1, 0)
        return income_eligible * (aged_head + aged_spouse) * aged_low_agi_exemption
