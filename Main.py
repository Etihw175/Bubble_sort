class BubbleSorter:
    def __init__(self, data):
        """
        ตัวสร้างคลาส รับข้อมูลเป็น list
        """
        self.data = data

    def display(self):
        """
        แสดงข้อมูลใน list
        """
        print(self.data)

    def bubble_sort(self):
            n = len(self.data)

            print("Before sorting:")
            print("Current data:", self.data)

            for i in range(n):
                swapped = False
                for j in range(0, n - i - 1):
                    if self.data[j] > self.data[j + 1]:
                        self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                        swapped = True

                print(f"After round {i+1}: {self.data}")

                if not swapped:
                    break

nums = [64, 34, 25, 12, 22, 11, 90] 
sorter = BubbleSorter(nums)
    
sorter.display()

sorter.bubble_sort()

print("After sorting : ")
sorter.display()