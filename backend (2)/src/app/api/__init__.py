"""Apis."""
from collections import namedtuple

from .card_payment import card_payment_blueprint
from .person import person_blueprint
from .eskk import eskk_blueprint
from .card import card_blueprint

BlueprintContainer = namedtuple("BlueprintContainer", ["obj", "url_prefix"])

blueprints = []
blueprints.append(BlueprintContainer(person_blueprint, "/api/person"))
blueprints.append(BlueprintContainer(eskk_blueprint, "/api/eskk"))
blueprints.append(BlueprintContainer(card_blueprint, "/api/card"))
blueprints.append(BlueprintContainer(card_payment_blueprint, "/api/card_payment"))