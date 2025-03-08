import java.io.*;
import java.util.*;

public class Matching {

    // 해시 테이블 선언
    private static HashTable<String, int[]> substringIndexTable = new HashTable<>();

    public static void main(String[] args) {
        BufferedReader userInputReader = new BufferedReader(new InputStreamReader(System.in));

        // 사용자 입력 반복 처리
        while (true) {
            try {
                String userCommand = userInputReader.readLine();
                if ("QUIT".equalsIgnoreCase(userCommand)) break;
                processUserCommand(userCommand);
            } catch (IOException e) {
                System.out.println("Invalid input: " + e.getMessage());
            }
        }
    }

    /**
     * 사용자 명령어 처리
     * @param command 사용자 명령어
     */
    private static void processUserCommand(String command) throws IOException {
        char commandType = command.charAt(0);
        String commandArgument = command.substring(2);

        switch (commandType) {
            case '<':
                loadFileIntoHashTable(commandArgument);
                break;
            case '@':
                displayHashTableSlot(Integer.parseInt(commandArgument));
                break;
            case '?':
                searchPatternInHashTable(commandArgument);
                break;
            default:
                System.out.println("Unknown command: " + commandType);
        }
    }

    /**
     * 파일 읽어서 해시 테이블에 로드
     * @param fileName 파일 이름
     */
    private static void loadFileIntoHashTable(String fileName) throws IOException {
        BufferedReader fileReader = new BufferedReader(new FileReader(fileName));
        substringIndexTable = new HashTable<>();
        String fileLine;
        int lineNumber = 1;

        while ((fileLine = fileReader.readLine()) != null) {
            for (int i = 0; i <= fileLine.length() - 6; i++) {
                String substring = fileLine.substring(i, i + 6);
                int[] position = {lineNumber, i + 1};
                substringIndexTable.add(substring, position);
            }
            lineNumber++;
        }
        fileReader.close();
    }

    /**
     * 특정 슬롯의 데이터를 출력
     * @param slotIndex 슬롯 인덱스
     */
    private static void displayHashTableSlot(int slotIndex) {
        List<String> storedSubstrings = substringIndexTable.getKeysAtSlot(slotIndex);
        if (storedSubstrings.isEmpty()) {
            System.out.println("EMPTY");
        } else {
            System.out.println(String.join(" ", storedSubstrings));
        }
    }

    /**
     * 패턴 검색
     * @param pattern 검색할 패턴
     */
    private static void searchPatternInHashTable(String pattern) {
        List<int[]> allOccurrences = findAllSubstringOccurrences(pattern);
        List<int[]> validOccurrences = filterValidPatternOccurrences(allOccurrences, pattern.length());

        if (validOccurrences.isEmpty()) {
            System.out.println("(0, 0)");
        } else {
            printPatternOccurrences(validOccurrences);
        }
    }

    /**
     * 패턴에서 모든 서브스트링 발생 위치 찾기
     * @param pattern 검색할 패턴
     * @return 서브스트링 발생 위치 목록
     */
    private static List<int[]> findAllSubstringOccurrences(String pattern) {
        int patternLength = pattern.length();
        List<int[]> occurrences = new ArrayList<>();

        for (int i = 0; i <= patternLength - 6; i++) {
            String substring = pattern.substring(i, i + 6);
            List<int[]> currentOccurrences = substringIndexTable.findValues(substring);

            if (i == 0) {
                occurrences.addAll(currentOccurrences);
            } else {
                occurrences.addAll(filterConsecutiveOccurrences(occurrences, currentOccurrences));
            }
        }

        return occurrences;
    }

    /**
     * 연속성을 만족하는 서브스트링 발생 위치 필터링
     * @param previousOccurrences 이전 서브스트링 발생 위치
     * @param currentOccurrences 현재 서브스트링 발생 위치
     * @return 연속성을 만족하는 발생 위치
     */
    private static List<int[]> filterConsecutiveOccurrences(List<int[]> previousOccurrences, List<int[]> currentOccurrences) {
        List<int[]> validOccurrences = new ArrayList<>();

        for (int[] currentOccurrence : currentOccurrences) {
            int[] previousPosition = {currentOccurrence[0], currentOccurrence[1] - 1};
            boolean isConsecutive = previousOccurrences.stream()
                .anyMatch(prev -> prev[0] == previousPosition[0] && prev[1] == previousPosition[1]);

            if (isConsecutive) {
                validOccurrences.add(currentOccurrence);
            }
        }

        return validOccurrences;
    }

    /**
     * 연속적인 패턴 발생 위치 필터링
     * @param occurrences 수집된 발생 위치
     * @param patternLength 패턴 길이
     * @return 최종 유효한 발생 위치
     */
    private static List<int[]> filterValidPatternOccurrences(List<int[]> occurrences, int patternLength) {
        Map<Integer, List<Integer>> groupedOccurrencesByLine = groupOccurrencesByLine(occurrences);
        List<int[]> validOccurrences = new ArrayList<>();

        for (Map.Entry<Integer, List<Integer>> entry : groupedOccurrencesByLine.entrySet()) {
            int lineNumber = entry.getKey();
            List<Integer> positions = entry.getValue();
            Collections.sort(positions);

            for (int start : positions) {
                if (isValidPatternStart(positions, start, patternLength)) {
                    validOccurrences.add(new int[]{lineNumber, start});
                }
            }
        }

        validOccurrences.sort(Comparator.comparingInt((int[] occurrence) -> occurrence[0]).thenComparingInt(occurrence -> occurrence[1]));
        return validOccurrences;
    }

    /**
     * 발생 위치를 라인별로 그룹화
     * @param occurrences 발생 위치
     * @return 라인별 그룹화된 발생 위치
     */
    private static Map<Integer, List<Integer>> groupOccurrencesByLine(List<int[]> occurrences) {
        Map<Integer, List<Integer>> groupedOccurrences = new HashMap<>();

        for (int[] occurrence : occurrences) {
            groupedOccurrences.computeIfAbsent(occurrence[0], key -> new ArrayList<>()).add(occurrence[1]);
        }

        return groupedOccurrences;
    }

    /**
     * 유효한 패턴 시작 위치인지 확인
     * @param positions 위치 목록
     * @param start 시작 위치
     * @param patternLength 패턴 길이
     * @return 유효한 패턴 여부
     */
    private static boolean isValidPatternStart(List<Integer> positions, int start, int patternLength) {
        for (int offset = 1; offset < patternLength - 5; offset++) {
            if (!positions.contains(start + offset)) {
                return false;
            }
        }
        return true;
    }

    /**
     * 발생 위치 출력
     * @param occurrences 발생 위치
     */
    private static void printPatternOccurrences(List<int[]> occurrences) {
        StringBuilder resultBuilder = new StringBuilder();
        for (int[] occurrence : occurrences) {
            resultBuilder.append(String.format("(%d, %d) ", occurrence[0], occurrence[1]));
        }
        System.out.println(resultBuilder.toString().trim());
    }
}
