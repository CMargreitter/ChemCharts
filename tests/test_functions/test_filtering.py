import unittest
import numpy as np

from chemcharts.core.container.chemdata import ChemData
from chemcharts.core.container.smiles import Smiles
from chemcharts.core.container.embedding import Embedding
from chemcharts.core.functions.filtering import Filtering


class TestFiltering(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        test_chemdata = ChemData(Smiles([""]), name="test_chemdata")
        embedding = Embedding(np.array([[1, 2],
                                        [2, 2],
                                        [4, 2],
                                        [2, 3],
                                        [2.6, 5],
                                        [11.2, 2],
                                        [5, 1.2],
                                        [4, 5],
                                        [8, 9],
                                        [1, 1],
                                        [15, 1],
                                        [5, 2],
                                        [6, 4],
                                        [6, 1],
                                        [4, 18],
                                        [3, 1],
                                        [1, 9],
                                        [6, 4],
                                        [3, 4],
                                        [7, 8]]))
        scores = [1, 3, 4, 5, 2, 1, 6, 3, 5, 0, 2, 1, 3, 4, 1, 2, 8, 6, 1, 1]

        test_chemdata.set_embedding(embedding)
        test_chemdata.set_scores(scores)
        cls.test_chemdata = test_chemdata

    def setUp(self) -> None:
        pass

    def test_filtering(self):
        test_filter = Filtering()
        filtered_chemdata = test_filter.filter_range(self.test_chemdata, range_dim1=(2, 12), range_dim2=(2, 12))
        embedding = filtered_chemdata.get_embedding()
        length_embedding = len(embedding)
        self.assertEqual(length_embedding, 24)
