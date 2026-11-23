# 0271. Encode and Decode Strings

- **Difficulty:** Medium
- **Topic:** Arrays & Hashing
- **Pattern:** Length-Prefixed String Chunking / Serialization Protocol
- **LeetCode Link:** [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) *(Premium / NeetCode 150 / LintCode 659)*

---

## Problem Statement

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement `encode` and `decode` methods:
* `encode(List<String> strs) -> String`
* `decode(String s) -> List<String>`

Strings may contain **any possible characters** out of 256 valid ASCII characters (including commas, colons, spaces, numbers, and delimiters).

### Examples

**Example 1:**
```text
Input: ["lint", "code", "love", "you"]
Output: ["lint", "code", "love", "you"]
Explanation:
One possible encoding: "4#lint4#code4#love3#you"
```

**Example 2:**
```text
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
```

---

## 💡 Intuition & Why Simple Delimiters Fail

If you join strings using a fixed separator like `","` or `";"`, what happens when a string itself contains `","`?
* Input: `["hello,world", "test"]`
* Joined: `"hello,world,test"`
* Decoded: `["hello", "world", "test"]` ❌ **Broken!**

### The Network Protocol Solution: Length-Prefixing
Prepend each string with its **character length** followed by a delimiter `#`:
$$\text{Encoded Chunk} = \text{length} + \text{"\#"} + \text{content}$$

Because the decoder reads the integer length first, it knows **exactly how many bytes/characters to jump forward**, making it 100% immune to any characters inside the content (even if the content contains `#`, numbers, or emojis)!

### Decoding Pointer Trace

```text
Encoded String:  "4 # l i n t 4 # c o d e"
Indices:          0 1 2 3 4 5 6 7 8 9 0 1
                  ▲ ▲         ▲
                  i j         next i = j + 1 + length = 1 + 1 + 4 = 6
                  
Step 1: Read i to j ('4'), find '#' at index 1 -> length = 4
Step 2: Slice s[2 : 2 + 4] = "lint"
Step 3: Jump i to index 6
Step 4: Repeat for next chunk
```

---

## 🚀 Implementations

### Python 3
```python
class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        result = []
        i = 0
        n = len(s)

        while i < n:
            # Find the '#' delimiter
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            start = j + 1
            end = start + length
            result.append(s[start:end])
            i = end

        return result
```

### Java
```java
import java.util.*;

public class Codec {
    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String s : strs) {
            sb.append(s.length()).append('#').append(s);
        }
        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> result = new ArrayList<>();
        int i = 0;
        int n = s.length();

        while (i < n) {
            int j = i;
            while (s.charAt(j) != '#') {
                j++;
            }
            int length = Integer.parseInt(s.substring(i, j));
            int start = j + 1;
            int end = start + length;
            result.add(s.substring(start, end));
            i = end;
        }

        return result;
    }
}
```

---

## 📊 Complexity Analysis

- **Time Complexity:**
  * `encode`: $O(N)$ where $N$ is the total number of characters across all strings.
  * `decode`: $O(N)$ because the pointer traverses each character at most twice (once for length, once during slice).
- **Space Complexity:** $O(1)$ auxiliary memory (excluding the output list and encoded string).
