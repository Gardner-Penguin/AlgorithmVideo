""" Valid Parenthese O(n) """
def get_is_parenthese(s):
    br_map = { '[': ']', '{': '}', '(': ')' }
    stack = []
    for char in s:
        is_left_br = char in br_map
        if is_left_br:
            stack.push(char)
            continue

        if not stack or br_map[stack[-1]] != char:
            return False
        else:
            stack.pop()
    return not stack

""" min/max Stack O(n) """
# public class StackWithMin2 extends Stack {
#     Stack s2;
#     public StackWithMin2() {
#         s2 = new Stack();    
#     }

#     public void push(int value) {
#         if (value <= min()) {
#             s2.push(value);
#         }
#         super.push(value);
#     }

#     public Integer pop() {
#         int value = super.pop();
#         if (value == min()) {
#             s2.pop();   
#         }
#         return value;
#     }

#     public int min() {
#         if (s2.isEmpty()) {
#             return Integer.MAX_VALUE;
#         } else {
#             return s2.peek();
#         }
#     }
# }
""" remove alphabet Duplicates O(n) """
# 쌓아나가며 탑이랑 비교