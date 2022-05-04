def count(hand):
        
        cnt =0;
        for h in hand:
            print(h);
            print('J');
            print(type(h));
            if h in ['J', 'Q', 'K']:
                cnt = cnt + 10;
            if cnt <=10 and h =='A':
                cnt = cnt + 11;
            else:
                print("string");
                cnt = cnt + int(h);
                
        return cnt;




 total = 0
    # Count the number of aces and deal with how to apply them at the end.
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            aces += 1
        else:
            # Convert number cards (e.g. '7') to ints
            total += int(card)
    # At this point, total is the sum of this hand's cards *not counting aces*.

    # Add aces, counting them as 1 for now. This is the smallest total we can make from this hand
    total += aces
    # "Upgrade" aces from 1 to 11 as long as it helps us get closer to 21
    # without busting
    while total + 10 <= 21 and aces > 0:
        # Upgrade an ace from 1 to 11
        total += 10
        aces -= 1
    return total