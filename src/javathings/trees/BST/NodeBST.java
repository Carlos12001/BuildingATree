package javathings.trees.BST;


import javathings.trees.abstracTree.TreeNode;

public class NodeBST extends TreeNode {

    public NodeBST(int token){
        super(token);
    }

    public NodeBST(int token, NodeBST left, NodeBST right){
        super(token, left, right);
    }
}