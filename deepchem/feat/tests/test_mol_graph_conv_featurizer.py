import unittest
import numpy as np
from deepchem.feat import MolGraphConvFeaturizer
from deepchem.feat import PagtnMolGraphFeaturizer


class TestMolGraphConvFeaturizer(unittest.TestCase):

  def test_default_featurizer(self):
    smiles = ["C1=CC=CN=C1", "O=C(NCc1cc(OC)c(O)cc1)CCCC/C=C/C(C)C"]
    featurizer = MolGraphConvFeaturizer()
    graph_feat = featurizer.featurize(smiles)
    assert len(graph_feat) == 2

    # assert "C1=CC=CN=C1"
    assert graph_feat[0].num_nodes == 6
    assert graph_feat[0].num_node_features == 30
    assert graph_feat[0].num_edges == 12

    # assert "O=C(NCc1cc(OC)c(O)cc1)CCCC/C=C/C(C)C"
    assert graph_feat[1].num_nodes == 22
    assert graph_feat[1].num_node_features == 30
    assert graph_feat[1].num_edges == 44

  def test_featurizer_with_use_edge(self):
    smiles = ["C1=CC=CN=C1", "O=C(NCc1cc(OC)c(O)cc1)CCCC/C=C/C(C)C"]
    featurizer = MolGraphConvFeaturizer(use_edges=True)
    graph_feat = featurizer.featurize(smiles)
    assert len(graph_feat) == 2

    # assert "C1=CC=CN=C1"
    assert graph_feat[0].num_nodes == 6
    assert graph_feat[0].num_node_features == 30
    assert graph_feat[0].num_edges == 12
    assert graph_feat[0].num_edge_features == 11

    # assert "O=C(NCc1cc(OC)c(O)cc1)CCCC/C=C/C(C)C"
    assert graph_feat[1].num_nodes == 22
    assert graph_feat[1].num_node_features == 30
    assert graph_feat[1].num_edges == 44
    assert graph_feat[1].num_edge_features == 11

  def test_featurizer_with_use_chirality(self):
    smiles = ["C1=CC=CN=C1", "O=C(NCc1cc(OC)c(O)cc1)CCCC/C=C/C(C)C"]
    featurizer = MolGraphConvFeaturizer(use_chirality=True)
    graph_feat = featurizer.featurize(smiles)
    assert len(graph_feat) == 2

    # assert "C1=CC=CN=C1"
    assert graph_feat[0].num_nodes == 6
    assert graph_feat[0].num_node_features == 32
    assert graph_feat[0].num_edges == 12

    # assert "O=C(NCc1cc(OC)c(O)cc1)CCCC/C=C/C(C)C"
    assert graph_feat[1].num_nodes == 22
    assert graph_feat[1].num_node_features == 32
    assert graph_feat[1].num_edges == 44

  def test_featurizer_with_use_partial_charge(self):
    smiles = ["C1=CC=CN=C1", "O=C(NCc1cc(OC)c(O)cc1)CCCC/C=C/C(C)C"]
    featurizer = MolGraphConvFeaturizer(use_partial_charge=True)
    graph_feat = featurizer.featurize(smiles)
    assert len(graph_feat) == 2

    # assert "C1=CC=CN=C1"
    assert graph_feat[0].num_nodes == 6
    assert graph_feat[0].num_node_features == 31
    assert graph_feat[0].num_edges == 12

    # assert "O=C(NCc1cc(OC)c(O)cc1)CCCC/C=C/C(C)C"
    assert graph_feat[1].num_nodes == 22
    assert graph_feat[1].num_node_features == 31
    assert graph_feat[1].num_edges == 44

  def test_featurizer_with_pos_kwargs(self):
    # Test featurizer with atom 3-D coordinates as kwargs
    smiles = ["C1=CC=CN=C1", "CC"]
    pos_x = [np.random.randn(6), np.random.randn(2)]
    pos_y, pos_z = pos_x, pos_x
    featurizer = MolGraphConvFeaturizer()
    graph_feat = featurizer.featurize(smiles,
                                      pos_x=pos_x,
                                      pos_y=pos_y,
                                      pos_z=pos_z)

    assert len(graph_feat) == 2
    assert graph_feat[0].num_nodes == 6
    assert graph_feat[0].pos.shape == (6, 3)
    assert graph_feat[1].num_nodes == 2
    assert graph_feat[1].pos.shape == (2, 3)


class TestPagtnMolGraphConvFeaturizer(unittest.TestCase):

  def test_default_featurizer(self):
    smiles = ["C1=CC=CN=C1", "O=C(NCc1cc(OC)c(O)cc1)CCCC/C=C/C(C)C"]
    featurizer = PagtnMolGraphFeaturizer(max_length=5)
    graph_feat = featurizer.featurize(smiles)
    assert len(graph_feat) == 2

    # assert "C1=CC=CN=C1"
    assert graph_feat[0].num_nodes == 6
    assert graph_feat[0].num_node_features == 94
    assert graph_feat[0].num_edges == 36
    assert graph_feat[0].num_edge_features == 42

    # assert "O=C(NCc1cc(OC)c(O)cc1)CCCC/C=C/C(C)C"
    assert graph_feat[1].num_nodes == 22
    assert graph_feat[1].num_node_features == 94
    assert graph_feat[1].num_edges == 484
    assert graph_feat[0].num_edge_features == 42
