__author__ = 'Jolin'
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from coin_info.data_collector import btcWallet

import json
import commonView


@login_required()
def syncTop100WalletData(request):
    btcWallet.syncData()
    return HttpResponse(json.dumps(commonView.reponseOK(), ensure_ascii=False))