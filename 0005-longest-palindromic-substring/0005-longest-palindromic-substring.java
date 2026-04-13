class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() < 1) return "";
        
        int start = 0, end = 0;

        for (int i = 0; i < s.length(); i++) {
            // 1. 홀수 길이 팰린드롬 체크 (중심이 문자 하나: "aba")
            int len1 = expandAroundCenter(s, i, i);
            // 2. 짝수 길이 팰린드롬 체크 (중심이 문자 사이: "abba")
            int len2 = expandAroundCenter(s, i, i + 1);
            
            int len = Math.max(len1, len2);
            
            // 기존에 찾은 길이보다 길면 인덱스 갱신
            if (len > end - start) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }
        
        return s.substring(start, end + 1);
    }

    private int expandAroundCenter(String s, int left, int right) {
        // 범위 내에 있고 양 끝 문자가 같으면 계속 확장
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        // while문을 빠져나올 때 이미 범위를 벗어났거나 문자가 다르므로 (right - left - 1)이 실제 길이
        return right - left - 1;
    }
}