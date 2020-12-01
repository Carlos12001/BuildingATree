package javathings.trees.abstracTree;


/**
 *
 */
public abstract class Tree {

    /**
     *
     */
    protected TreeNode root;
    /**
     *
     */
    private String treeID;

    /**
     *
     */
    protected String current;

    /**
     *
     */
    protected int[] currentArray;

    public Tree() {
        this.root = null;
        this.current = null;
    }

    public boolean isEmpty(){
        return this.root == null;
    }

    public void append(String nodeID){
        String[] tmp = nodeID.split("@");

        if(tmp[0].equals(this.treeID)){
            appendAux(Integer.parseInt(tmp[1]));
        } else{
            this.current = null;
            this.root = null;
        }
    }

    protected abstract void appendAux(int key);

    public abstract void setCurrent();

    protected abstract String getCurrent();

    /**
     * Sets new treeID.
     *
     * @param treeID New value of treeID.
     */
    public void setTreeID(String treeID) {
        this.treeID = treeID;
    }

    /**
     * Gets treeID.
     *
     * @return Value of treeID.
     */
    public String getTreeID() {
        return treeID;
    }

    /**
     * Sets new currentArray.
     *
     * @param currentArray New value of currentArray.
     */
    public void setCurrentArray(int[] currentArray) {
        this.currentArray = currentArray;
    }

    /**
     * Gets currentArray.
     *
     * @return Value of currentArray.
     */
    public int[] getCurrentArray() {
        return currentArray;
    }
}