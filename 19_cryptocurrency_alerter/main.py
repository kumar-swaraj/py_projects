from crypto_data import Coin, get_coins


def alert(symbol: str, bottom: float, top: float, coins_list: list[Coin]) -> None:
    """Creates an alert for the given price range of a coin."""

    for coin in coins_list:
        if coin.symbol.lower() == symbol.lower():
            if coin.current_price >= top or coin.current_price <= bottom:
                print(coin, "!!!TRIGGER!!!")
            else:
                print(coin)


if __name__ == "__main__":
    coins = get_coins()

    alert(symbol="btc", bottom=100_000, top=120_000, coins_list=coins)
    alert(symbol="eth", bottom=5_000, top=10_000, coins_list=coins)
    alert(symbol="xrp", bottom=1, top=2, coins_list=coins)
