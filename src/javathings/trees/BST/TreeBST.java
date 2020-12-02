package javathings.trees.BST;

import javathings.trees.abstracTree.Tree;
import javathings.trees.abstracTree.TreeNode;

public class TreeBST extends Tree {

//    public static void main(String[] args) {
//        TreeBST arbol = new TreeBST();
//        arbol.insert(3);
//        arbol.insert(5);
//        arbol.insert(1);
//        arbol.insert(34);
//        arbol.insert(0);
//        System.out.println(arbol.contains(0));
//    }

    private NodeBST root;

    public TreeBST(){
       super();
       setTreeID("treeBST");
    }

    public void insert(int key){
        this.root = insertAux(key, this.root);
    }

    private NodeBST insertAux(int key, NodeBST tree){
        if (tree == null){
            tree = new NodeBST(key);
            return tree;
        } else if (key < tree.getToken()){
            tree.setLeft(insertAux(key, (NodeBST) tree.getLeft()));
        } else if (key > tree.getToken()){
            tree.setRight(insertAux(key, (NodeBST) tree.getRight()));
        }
        return tree;
    }

    public boolean contains(int element) {
        return this.contains(element, this.root);
    }

    private boolean contains(int element, NodeBST node) {
        if (node == null) {
            return false;
        } else {
            if (element < node.getToken())
                return contains(element, (NodeBST) node.getLeft());
            else if (element > node.getToken())
                return contains(element, (NodeBST) node.getRight());
            else
                return true;
        }
    }

    @Override
    protected void appendAux(int key) {
        this.insert(key);
    }
}
