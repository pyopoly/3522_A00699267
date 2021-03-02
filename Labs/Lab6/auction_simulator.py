"""
Implements the observer pattern and simulates a simple auction.
"""
import random


class Auctioneer:
    """
    The auctioneer acts as the "core". This class is responsible for
    tracking the highest bid and notifying the bidders if it changes.
    """

    def __init__(self):
        self._bidders = []
        self._highest_bid = 0
        self._highest_bidder = None

    def register_bidder(self, bidder):
        """
        Adds a bidder to the list of tracked bidders.
        :param bidder: object with __call__(auctioneer) interface.
        """
        self._bidders.append(bidder)

    def reset_auctioneer(self):
        """
        Resets the auctioneer. Removes all the bidders and resets the
        highest bid to 0.
        """
        self._highest_bid = 0
        self._highest_bidder = None
        self._bidders.clear()

    def _notify_bidders(self):
        """
        Executes all the bidder callbacks. Should only be called if the
        highest bid has changed.
        """
        for bidder in self._bidders:
            bidder(self)

    def accept_bid(self, bid, bidder="Starting Bid"):
        """
        Accepts a new bid and updates the highest bid. This notifies all
        the bidders via their callbacks.
        :param bid: a float.
        :precondition bid: should be higher than the existing bid.
        :param bidder: The object with __call__(auctioneer) that placed
        the bid.
        """
        self._highest_bid = bid
        self._highest_bidder = bidder
        self._notify_bidders()

    def get_bidders(self):
        """
        Getter for Bidders in this auction.
        :return list of Bidders
        """
        return self._bidders

    def get_highest_bid(self):
        """
        Returns the the highest bid currently in the auction.
        :return: a double, the current highest bid in the auction
        """
        return self._highest_bid

    def get_highest_bidder(self):
        """
        Returns the current highest Bidder in the auction
        :return: a Bidder
        """
        return self._highest_bidder

    highest_bid = property(get_highest_bid)
    highest_bidder = property(get_highest_bidder)


class Bidder:
    """
    • name
        The name of the bidder
    • budget
        The amount in money that the bidder is willing to spend.
        The bidder will not make a bid greater than this amount.
    • bid_probability
        This is a floating point value between 0 and 1. This represents the percentage probability chance that
        this bidder will retaliate to a bid with their own bid.
    • bid_increase_perc
        This is a number greater than 1 . A value of 1.4 translates to 140%.
        This percentage is the value of the new bid that the bidder places. For example,
        if the bidder has a bid_increase_perc value of 1.5 (that is, 150%) then if this bidder were to place a bid,
        it would be 1.5 times the current highest bid on the item.
    • highest_bid
        The highest bid amount that was bid by this bidder.
    """
    def __init__(self, name, money=100, bid_probability=0.35, bid_increase=1.1):
        self._name = name
        # self._threat_chance = threat_chance
        self._budget = money
        self._bid_increase_perc = bid_increase
        self._bid_probability = bid_probability
        self._highest_bid = 0

    def __call__(self, auctioneer):
        """
        Places a new bid with auctioneer (cause a new bid, causing auctioneer to notify all observers again).
        Note:
            • The bid is against another bidder and not against themselves
            • The amount that they bid (dictated by bid_increase_perc is not greater than their budget
            • After accounting for their bid_probability . (Hint: use the random.random() method to generate a random float between 0 and 1 (exclusive) )
        :param auctioneer:
        :return: None
        """
        if auctioneer.highest_bidder is not self:
            bid_probability = random.random()
            next_bid = round(auctioneer.highest_bid * self._bid_increase_perc, 2)
            if bid_probability < self._bid_probability and next_bid < self._budget:
                print(f"{self} bidded {next_bid} in response to {auctioneer.highest_bidder}'s bid of {auctioneer.highest_bid}")
                self._highest_bid = next_bid
                auctioneer.accept_bid(next_bid, self)

    def get_name(self):
        """ Getter to get this Bidder's name as a string. """
        return self._name

    def get_highest_bid(self):
        """ Getter to get this Bidder's highest bid as a double. """
        return self._highest_bid

    def __str__(self):
        """ Formatted toString. """
        return self._name

    name = property(get_name)
    highest_bid = property(get_highest_bid)


class Auction:
    """
    Simulates an auction. Is responsible for driving the auctioneer and
    the bidders.
    """

    def __init__(self, bidders):
        """
        Initialize an auction. Requires a list of bidders that are
        attending the auction and can bid.
        :param bidders: sequence type of objects of type Bidder
        """
        self._item = None
        self._auctioneer = Auctioneer()
        for bidder in bidders:
            self._auctioneer.register_bidder(bidder)

    def simulate_auction(self, item, start_price):
        """
        Starts the auction for the given item at the given starting
        price. Drives the auction till completion and prints the results.
        :param item: string, name of item.
        :param start_price: float
        """
        self._item = item
        print(f"Auctioning {item} starting at {start_price}")
        self._auctioneer.accept_bid(start_price)
        print(f"\nThe winner of the auction is: {self._auctioneer.highest_bidder} at {self._auctioneer.highest_bid}\n")
        self.print_bid_summary()

    def print_bid_summary(self):
        """
        Prints conclusion information of this auction, which is the names
        of all bidders and the highest bids they made.
        """
        print("Highest Bids Per Bidder")
        info = ((bidder, bidder.highest_bid) for bidder in self._auctioneer._bidders)
        for bidder, highest_bid in info:
            print("Bidder: {:10} Highest Bid: {}".format(str(bidder), highest_bid))


def main():
    bidders = []

    # Hardcoding the bidders.
    bidders.append(Bidder("Jojo", 3000, random.random(), 1.2))
    bidders.append(Bidder("Melissa", 7000, random.random(), 1.5))
    bidders.append(Bidder("Priya", 15000, random.random(), 1.1))
    bidders.append(Bidder("Kewei", 800, random.random(), 1.9))
    bidders.append(Bidder("Scott", 4000, random.random(), 2))

    print("\n\nStarting Auction!!")
    print("------------------")
    my_auction = Auction(bidders)
    my_auction.simulate_auction("Antique Vase", 100)


if __name__ == '__main__':
    main()

