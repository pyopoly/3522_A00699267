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
        self.bidders = []
        self._highest_bid = 0
        self._highest_bidder = None

    def register_bidder(self, bidder):
        """
        Adds a bidder to the list of tracked bidders.
        :param bidder: object with __call__(auctioneer) interface.
        """
        pass

    def reset_auctioneer(self):
        """
        Resets the auctioneer. Removes all the bidders and resets the
        highest bid to 0.
        """
        pass

    def _notify_bidders(self):
        """
        Executes all the bidder callbacks. Should only be called if the
        highest bid has changed.
        """
        pass

    def accept_bid(self, bid, bidder="Starting Bid"):
        """
        Accepts a new bid and updates the highest bid. This notifies all
        the bidders via their callbacks.
        :param bid: a float.
        :precondition bid: should be higher than the existing bid.
        :param bidder: The object with __call__(auctioneer) that placed
        the bid.
        """
        pass


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
    def __init__(self, name, money=100, threat_chance=0.35, bid_increase=1.1):
        self.name = name
        self.threat_chance = threat_chance
        self.money = money
        self.bid_increase = bid_increase
        self.highest_bid = 0

    def __call__(self, auctioneer):
        pass

    def __str__(self):
        return self.name


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
        pass

    def simulate_auction(self, item, start_price):
        """
        Starts the auction for the given item at the given starting
        price. Drives the auction till completion and prints the results.
        :param item: string, name of item.
        :param start_price: float
        """
        pass


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

