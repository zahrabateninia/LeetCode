// 2490

// A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

// For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
// Words consist of only uppercase and lowercase English letters. Uppercase and lowercase 
// English letters are considered different.

// A sentence is circular if:

// The last character of each word in the sentence is equal to the first character of its next word.
// The last character of the last word is equal to the first character of the first word.
// For example, "leetcode exercises sound delightful"

const isCircularSentence = function(sentence) {
    const words = sentence.split(" ");

    for (let i = 0; i < words.length; i++) {
        if (words[i].at(-1) !== words[(i + 1) % words.length][0]) { // when we reach the last word, we need to return to the first word
            return false;
        }
    }

    return true;
};

// imp: use compare adjacent elements while using modulo to handle circular relationships.