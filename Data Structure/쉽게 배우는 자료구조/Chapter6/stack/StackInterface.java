package stack;

public interface StackInterface<E> {
    public void push(E newItem);
    public E pop();
    public E top();
    public boolean isEmmpty();
    public void popAll();
}