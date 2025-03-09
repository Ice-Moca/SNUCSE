
public class Hanoi {

    // 하노이탑 문제를 해결하는 재귀 함수
    public static void solveHanoi(int n, String from, String to, String aux) {
        if (n == 1) {
            // 원반이 하나일 때는 그냥 이동
            System.out.println("Move disk 1 from " + from + " to " + to);
            return;
        }
        
        // n-1개의 원반을 보조 기둥으로 이동
        solveHanoi(n - 1, from, aux, to);
        
        // 가장 큰 원반을 목표 기둥으로 이동
        System.out.println("Move disk " + n + " from " + from + " to " + to);
        
        // n-1개의 원반을 보조 기둥에서 목표 기둥으로 이동
        solveHanoi(n - 1, aux, to, from);
    }

    public static void main(String[] args) {
        int n = 3; // 원반의 수
        System.out.println("The sequence of moves to solve the Hanoi Tower problem with " + n + " disks:");
        solveHanoi(n, "A", "C", "B"); // A -> 출발 기둥, B -> 보조 기둥, C -> 목표 기둥
    }
}

