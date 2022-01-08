from openfisca_us.model_api import *


class person_id(Variable):
    value_type = int
    entity = Person
    label = u"Unique reference for this person"
    definition_period = ETERNITY
