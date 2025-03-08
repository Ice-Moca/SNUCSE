import java.util.LinkedList;

public class AVLNode<T, E> {
    T key; // 키 값
    LinkedList<E> values; // 동일 키의 데이터 리스트
    AVLNode<T, E> left, right; // 왼쪽 및 오른쪽 자식 노드
    int height; // 노드 높이

    // 생성자
    AVLNode(T key, E value) {
        this.key = key;
        this.values = new LinkedList<>();
        this.values.add(value);
        this.height = 1;
    }

    // 동일 키 데이터 추가
    public void addValue(E value) {
        values.add(value);
    }
}
