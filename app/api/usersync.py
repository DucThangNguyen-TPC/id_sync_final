from flask import request, make_response
from sqlalchemy import exc

from app import db
from app.models import IdPair
from app.api import bp


@bp.route('/usersync', methods=['GET'])
def create_id_pair():
    """
        Insert the pair of battle net id and corresponding
        """
    # Get the incoming data
    query = request.args

    partner = query.get('partner')
    battle_net_id = query.get('buyer_user_id')
    beeswax_id = query.get('beeswax_id')

    # Check if the request coming from beeswax
    if partner is None or partner != 'beeswax':
        return make_response('Request denied: Request from invalid source', 200)
    else:
        id_pair = IdPair(battle_net_id=battle_net_id, beeswax_id=beeswax_id)
        try:
            db.session.add(id_pair)
            db.session.commit()
            return make_response('The following pair is successfully inserted into database:'
                                 '{} Battle net ID: {}'
                                 '{} Beeswax ID: {}'.format('\n', battle_net_id, '\n', beeswax_id), 200)
        except exc.IntegrityError:
            return make_response('The pair of Battle net Id and corresponding Beeswax Id is already stored', 200)
