from flask import jsonify, make_response
from app.models import IdPair
from app.api import bp


@bp.route('/beeswax/<battle_net_id>', methods=['GET'])
def get_beeswax_id(battle_net_id):
    """
    Get the beeswax ID from the given battle net id
    """
    # Get the incoming data
    id_pairs_from_battle_net_id = IdPair.query.filter_by(battle_net_id=battle_net_id).all()

    # Store the result in dictionary
    result = {'beeswax_ids': [id_pair.beeswax_id for id_pair in id_pairs_from_battle_net_id]}

    return make_response(jsonify(result))
