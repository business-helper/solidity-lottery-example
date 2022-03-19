# 0.19
# 190000000000000000

from brownie import Lottery, accounts, config, network
from web3 import Web3
from scripts.deploy_lottery import deploy_lottery
from scripts.helper import LOCAL_BLOCKCHAIN_ENVIRONMENTS
import pytest

def test_get_entrance_fee():
  if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
    pytest.skip()

  # Arrange
  lottery = deploy_lottery()
  # Act
  # 2,000
  # usdEntryFee is 50
  expected_entrance_fee_min = Web3.toWei(0.015, "ether")
  expected_entrance_fee_max = Web3.toWei(0.026, "ether")

  entrance_fee = lottery.getEntranceFee()
  print(f"[Entrance Fee] {entrance_fee}")
  # Assert
  assert expected_entrance_fee_min < entrance_fee
  assert expected_entrance_fee_max > entrance_fee


