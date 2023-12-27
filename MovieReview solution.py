import csv
import datetime
from load_words import load_words


class Review(object):

    def __init__(self, movie_title, review_content, directors, original_release_date):
        """ Copy and Paste your previous code in Task 2.2.1 """
        ###################################################
        ##### COPY YOUR PREVIOUS TASK 2.2.1 CODE HERE #####
        self.movie_title = str(movie_title)
        self.review_content = str(review_content)
        self.directors = list(directors)
        self.original_release_date = str(original_release_date)
        ###################################################

    def __str__(self):
        """ Copy and Paste your previous code in Task 2.2.2 """
        ###################################################
        ##### COPY YOUR PREVIOUS TASK 2.2.2 CODE HERE #####
        return (f'Review for {self.movie_title} ({self.original_release_date}): {self.review_content}')
        ###################################################

    def get_word_counts(self, words):
        """ Copy and Paste your previous code in Task 3.1 """
        #################################################
        ##### COPY YOUR PREVIOUS TASK 3.1 CODE HERE #####
        number_words = []
        for word in words:
            frequency = 0
            for others in self.review_content.split():
                if word == others:
                    frequency += 1
            number_words.append(frequency)
        return number_words
        #################################################

    def get_sentiment_score(self, positive_words, negative_words):
        """ Copy and Paste your previous code in Task 3.2 """
        #################################################
        ##### COPY YOUR PREVIOUS TASK 3.2 CODE HERE #####
        score = 0
        review = self.review_content.split()
        for word in review:
            if word in positive_words:
                score += 1
            if word in negative_words:
                score -= 1
        return score
        #################################################

    def is_directed_by(self, director):
        """
        Task 4.1.1
            Check whether the movie was directed by the director.

        Arg:
            director (str): director of the movie to find

        Return
            result (bool): whether the director is included in the directors of the movie

        Exception
            If director is an empty string, return True
        """
        ######################################
        ##### TODO: Write your code here #####

        return director in self.directors or director == ''

        ######################################

    def is_released_after(self, date):
        """
        Task 4.1.2
            Check whether the movie was released after the date.

        Arg:
            date (str): date of the form "yyyy-mm-dd" to filter

        Return
            result (bool): whether the movie was released after the date

        Exception
            If date is not of the form "yyyy-mm-dd", or date is not valid, return True
            Please refer to the description to check whether a date is valid or not.
        """
        ######################################
        ##### TODO: Write your code here ##### try:
        try:
            release = datetime.datetime.strptime(self.original_release_date, "%Y-%m-%d")
            date2 = datetime.datetime.strptime(date, "%Y-%m-%d")
            if release <= date2:
                return False
            else:
                return True
        except:
            return True

        ######################################


class Explorer(object):

    def __init__(self, reviews):
        """
        Task 4.2.1
            Initialize a Explorer object with the following attribute:
                reviews (list[Reviews]): list of the filtered Review objects

        Arg:
            reviews (list[Reviews]): list of Review objects to initialize with

        Return
            None (NoneType)
        """
        ######################################
        ##### TODO: Write your code here #####
        self.reviews = reviews

        ################viewer=self.reviews######################

    def __str__(self):
        if len(self.reviews) == 0:
            return "No review found in this explorer"
        else:
            return "\n".join(map(str, self.reviews))

    def filter_reviews_directed_by(self, director):
        """
        Task 4.2.2
            Update the reviews attribute by leaving only the reviews for the movies directed by the director.
            The updated reviews attribute should follow the order of the original one.
            Hint: Use is_directed_by method of the Review object.

        Arg:
            director (str): director of the movie to find

        Return
            None (NoneType)

        Exception
            If director is an empty string, preserve the reviews attribute
        """
        ######################################
        ##### TODO: Write your code here #####
        pass
        if director == '':
            return
        filtered = []
        for review in self.reviews:
            if review.is_directed_by(director):
                filtered.append(review)
        self.reviews = filtered
        ######################################

    def filter_reviews_released_after(self, date):
        """
        Task 4.2.3
            Update the reviews attribute by leaving only the reviews for the movies released after the date.
            The updated reviews attribute should follow the order of the original one.
            Hint: Use is_released_after method of the Review object.

        Arg:
            date (str): date of the form "yyyy-mm-dd" to filter

        Return
            None (NoneType)

        Exception
            If date is not of the form "yyyy-mm-dd", or date is not valid, preserve the reviews attribute.
        """
        ######################################
        ##### TODO: Write your code here #####
        pass
        filtered = []
        for review in self.reviews:
            if review.is_released_after(date):
                filtered.append(review)
        self.reviews = filtered
        ######################################

    def get_sentiment_scores(self, positive_words, negative_words):
        """
        Task 4.3.1
            Compute the sentiment scores of the reviews.
            The computed sentiment scores should follow the order of the reviews attribute.
            Hint: Use get_sentiment_score method of the Review object.

        Args:
            positive_words (list[str]): list of positive words
            negative_words (list[str]): list of negative words

        Return
            sentiment_scores (list[int]): list of sentiment scores of the reviews
        """
        ######################################
        ##### TODO: Write yo
        return [x.get_sentiment_score(positive_words, negative_words) for x in self.reviews]
        # for review in self.reviews:
        #     x=review.get_most_positive_review(self,positive_words,negative_words)

        pass
        ######################################

    def get_most_positive_review(self, positive_words, negative_words):
        """
        Task 4.3.2
            Find one of the mos
            pair=word,scoret positive reviews, i.e., reviews with the highest sentiment score.
            You should consider the case where the Explorer object contains no Review object.
            Hint: Use get_sentiment_scores method of the Explorer object.

        Args:
            positive_words (list[str]): list of positive words
            negative_words (list[str]): list of negative words

        Return
            most_positive_review (Review or str): one of the reviews with the highest sentiment score

        Exception
            If the Explorer object contains no Review object, return the string "No review found in this explorer".

        """
        #################
        if len(self.reviews) == 0:
            return "No review found in this explorer"  #########
        sent = self.get_sentiment_scores(positive_words, negative_words)
        index = sent.index(max(sent))
        return self.reviews[
            index]  ###urn max([x.get_sentiment_score(positive_words, negative_words) for x in selrevf.reviews ])#########
        ##### TODO: Write your code here #####
        pass

        ######################################


def preprocess_review_content(review_content):
    """ Copy and Paste your previous code for convert_reviews_to_objects in Task 2.1 """
    #################################################
    ##### COPY YOUR PREVIOUS TASK 2.1 CODE HERE #####
    pass
    #################################################


def convert_reviews_to_objects(file_path):
    """ Copy and Paste your previous code for convert_reviews_to_objects in Task 2.3 """
    #################################################
    ##### COPY YOUR PREVIOUS TASK 2.3 CODE HERE #####
    pass
    #################################################


def main():
    # You can modify below and test with your code.

    # Test code for Task 4.1
    print("###### Test for Task 4.1 ######")
    review_1 = Review(movie_title="10,000 B.C",
                      review_content="too dumb to take seriously but just silly enough to be sort of fun",
                      directors=["Roland Emmerich"],
                      original_release_date="2008-03-07")

    review_2 = Review(movie_title="Tarzan, the Ape Man",
                      review_content="not even funny as modern irony",
                      directors=["John Derek"],
                      original_release_date="1981-07-24")

    print(review_1.is_directed_by("Roland Emmerich"))
    print(review_1.is_released_after("2008-02-08"))
    print(review_2.is_directed_by("Roland Emmerich"))
    print(review_2.is_released_after("2008-02-08"))
    print()

    # Test code for Task 4.2
    print("###### Test for Task 4.2 ######")
    explorer = Explorer(reviews=[review_1, review_2])
    print(explorer)
    explorer.filter_reviews_directed_by("John Derek")
    print(explorer)
    explorer.filter_reviews_released_after("2000-01-01")
    print(explorer)
    print()

    # Test code for Task 4.3
    print("###### Test for Task 4.3 ######")
    explorer = Explorer(reviews=[review_1, review_2])
    print(explorer.get_sentiment_scores(["fun", "funny"], ["dumb", "silly"]))
    print(explorer.get_most_positive_review(["fun", "funny"], ["dumb", "silly"]))

    # A usage of the Explorer.
    print("###### A usage of the Explorer ######")
    print("Which director's movie reviews do you want to find? (Skip to find all)")
    print("Choose one: (1) Roland Emmerich; (2) John Derek; (3) Chris Columbus; or any name of director")
    director = input(">>> ")
    print("What date do you want to find movie reviews released after? (Skip to find all)")
    print("Choose one: (1) 1980-01-01; (2) 1990-01-01; (3) 2000-01-01; or any date of form yyyy-mm-dd")
    date = input(">>> ")

    if director in {"1", "2", "3", "(1)", "(2)", "(3)"}:
        director = {"1": "Roland Emmerich", "(1)": "Roland Emmerich",
                    "2": "John Derek", "(2)": "John Derek",
                    "3": "Chris Columbus", "(3)": "Chris Columbus"}[director]

    if date in {"1", "2", "3", "(1)", "(2)", "(3)"}:
        date = {"1": "1980-01-01", "(1)": "1980-01-01",
                "2": "1990-01-01", "(2)": "1990-01-01",
                "3": "2000-01-01", "(3)": "2000-01-01"}[date]

    option = ""
    while not option in {"1", "2", "(1)", "(2)"}:
        print("Choose one: (1) See all reviews; (2) See the most positive review")
        option = input(">>> ")

    explorer = Explorer(reviews=convert_reviews_to_objects("reviews.csv"))
    explorer.filter_reviews_directed_by(director)
    explorer.filter_reviews_released_after(date)

    if option in {"1", "(1)"}:
        print(explorer)
    if option in {"2", "(2)"}:
        positive_words, negative_words = load_words("words.csv")
        print(explorer.get_most_positive_review(positive_words, negative_words))


if __name__ == "__main__":
    main()
