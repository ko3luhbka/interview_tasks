from datetime import datetime
from collections import Counter


def trades_to_list(source='exchange_trades/trades.csv'):
    with open(source) as f:
        trades_list = []
        for line in f:
            line = line.strip().split(',')
            datetime_obj = datetime.strptime(line[0], '%H:%M:%S.%f')
            trades_list.append((datetime_obj, line[-1]))
    return trades_list


def find_max_trades_num(trades_list=trades_to_list()):
    max_exchange_trades = Counter()
    curr_exchange_trades = Counter()
    # The dict stores exchange names as keys, index of 1-minute window start
    # time in `trades_list` as values. For example:
    # {'V': i, 'D': j}, where i, j are indexes in list `trades_list`.
    exchange_start_time = {}

    trade_num = 0
    while trade_num < len(trades_list):
        curr_exchange = trades_list[trade_num][1]
        curr_trade_time = trades_list[trade_num][0]
        print(trade_num, '###', str(curr_trade_time), '###', curr_exchange)

        if curr_exchange not in exchange_start_time:
            exchange_start_time[curr_exchange] = trade_num

        delta = (curr_trade_time - trades_list[exchange_start_time[curr_exchange]][0])
        print('=== delta: ', delta.seconds)
        if delta.seconds < 60:
            curr_exchange_trades[curr_exchange] += 1
            trade_num += 1
            max_exchange_trades[curr_exchange] = max(
                curr_exchange_trades[curr_exchange],
                max_exchange_trades[curr_exchange],
            )
        else:
            max_exchange_trades[curr_exchange] = max(
                curr_exchange_trades[curr_exchange],
                max_exchange_trades[curr_exchange],
            )
            curr_exchange_trades[curr_exchange] = 0
            exchange_start_time[curr_exchange] += 1
        print('=== exchange_start_time: ', exchange_start_time)
        print('=== max_exchange_trades: ', max_exchange_trades)
        print('=== curr_exchange_trades: ', curr_exchange_trades)

    for _, trade in sorted(max_exchange_trades.items()):
        print(trade)
    print('=== exchange_start_time:', exchange_start_time)


find_max_trades_num()
