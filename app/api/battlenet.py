from flask import jsonify, make_response
from app.models import IdPair
from app.api import bp


@bp.route('/battle_net/<beeswax_id>', methods=['GET'])
def get_battle_net_id(beeswax_id):
    """
    Get the beeswax ID from the given battle net id
    """
    # Get the incoming data
    id_pairs_from_beeswax_id = IdPair.query.filter_by(beeswax_id=beeswax_id).all()

    # Store the result in dictionary
    result = {'battle_net_ids': [id_pair.battle_net_id for id_pair in id_pairs_from_beeswax_id]}

    return make_response(jsonify(result))
