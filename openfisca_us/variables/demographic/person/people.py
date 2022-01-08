from openfisca_us.model_api import *


class people(Variable):
    value_type = float
    entity = Person
    label = u"People represented"
    definition_period = YEAR
    default_value = 1.0
