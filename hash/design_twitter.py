# User function Template for python3
from collections import defaultdict, deque
from typing import List
class Twitter:
    # Compose a new tweet
    def postTweet(self, userId: int, tweetId: int):
        # Code here
        # le file d'attente est un dictionnaire
        self.tweet = defaultdict(deque)
        # ajout de la valeur tweetId avec pour clé userId
        self.tweet[userId].append(tweetId)
        # on renvoie les 10 derniers tweet
        if len(self.tweet[userId]) > 10:
            self.tweet[userId].pop()



    # Retrieve the 10 most recent tweet ids as mentioned in question
    def getNewsFeed(self, userId: int):
        # Code here
        
        pass


    # Follower follows a followee. If the operation is invalid, it should be a no-op.
    def follow(self, followerId: int, followeeId: int):
        # Code here
        pass

    # Follower unfollows a followee. If the operation is invalid, it should be a no-op.
    def unfollow(self, followerId: int, followeeId: int):
        # Code here
        pass


# {
# Driver Code Starts.
if __name__ == '__main__':
    obj = Twitter()
    totalQueries = int(input())
    for _ in range(totalQueries):
        query = list(map(int, input().split()))
        if (query[0] == 1):
            userId, tweetId = query[1], query[2]
            obj.postTweet(userId, tweetId)
        elif (query[0] == 2):
            userId = query[1]
            vec = obj.getNewsFeed(userId)
            for val in vec:
                print(val, end=' ')
            print()
        elif (query[0] == 3):
            follower, followee = query[1], query[2]
            obj.follow(follower, followee)
        else:
            follower, followee = query[1], query[2]
            obj.unfollow(follower, followee)
# } Driver Code Ends