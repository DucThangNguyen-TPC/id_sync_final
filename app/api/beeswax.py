from flask import jsonify, make_response
from app.models import IdPair
from app.api import bp


@bp.route('/beeswax/<beeswax_id>', methods=['GET'])
def get_beeswax_id(beeswax_id):
    """
    Get the beeswax ID from the given battle net id
    """
    # Get the incoming data
    id_pairs = IdPair.query.filter_by(beeswax_id=beeswax_id).all()

    # Store the result in dictionary
    result = {'beeswax_id': beeswax_id,
              'battle_net_id_associated': [id_pair.battle_net_id for id_pair in id_pairs]}

    return make_response(jsonify(result))
