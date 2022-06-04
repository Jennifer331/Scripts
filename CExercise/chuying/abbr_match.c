#include<stdio.h>
#include<ctype.h>

#define MAX_LEN 256

int next(char s[], int p) {
    if (isdigit(s[p])) {
        int acc = s[p] - '0';
        while (isdigit(s[++p])) {
            acc *= 10;
            acc += s[p] - '0';
        }
        return acc;
    } else {
        return 0;
    }
}

int len(int num) {
    int ans = 0;
    while (num > 0) {
        ans++;
        num /= 10;
    }
    return ans;
}

void main() {
    char s1[MAX_LEN], s2[MAX_LEN];
    int p1 = 0, p2 = 0;

    scanf("%s %s", s1, s2);

    while (1) {
        int c1 = next(s1, p1);
        int c2 = next(s2, p2);

        if (c2 > 0) {
            p1 += c2;
            p2 += len(c2);
        } else if (s1[p1] == s2[p2]) {
            if (s1[p1] == '\0')
                break;
            p1++;
            p2++;
        } else {
            return 0;
        }
    }

    return 1;
}
