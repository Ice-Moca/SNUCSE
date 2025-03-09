package stack;

public interface StackInterface<E> {
    public void push(E newItem);
    public E pop();
    public E top();
    public boolean isEmpty();
    public void popAll();
}