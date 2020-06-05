"""
Any estimators will be provided here.
"""
import items as items
import laplace as laplace


class AEstimator:
    """
    An estimator class will estimate the probability of a given variable.
    """

    def train(self, data):
        """
        Train the estimator using the given data.
        :param data: The data to use for the training. The data should be split into (evidence, history) with evidence
        being the evidence presented and history the history preceding the evidence. In this way on can, for example,
        classify unigrams, bigrams and n-grams.
        :return: Nothing
        """
        raise NotImplemented( 'The train method is not yet implemented' )

    def p(self, evidence, history=None):
        """
        Return the likelihood of evidence, given the history.
        :param history: The history to take into consideration
        :param evidence: The variable to test
        :return: The likelihood of evidence
        """
        raise NotImplemented('The P method is not implemented yet.')

    def _contents(items, laplace=False):
        # count occurrences of values
        print (items)
        counts = {}
        for item in items:
            counts[item] = counts.get(item,0) + 1.0
            # normalize
            for k in counts:
                if laplace:
                    counts[k] += 1.0
                    counts[k] /= (len(items) + len(counts))
                else:
                    counts[k] /= len(items)
            return counts


