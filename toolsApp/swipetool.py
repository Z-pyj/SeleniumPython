class moveDemo:
    def __init__(self, driver):
        self.driver = driver
        self.sizes = self.driver.get_window_size()

    def swipeUp(self, t=1000, n=1):
        """向上滑动屏幕"""
        x1 = self.sizes['width'] * 0.5
        y1 = self.sizes['height'] * 0.75
        y2 = self.sizes['height'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipeDown(self, t=1000, n=1):
        """向下滑动屏幕"""
        x1 = self.sizes['width'] * 0.5
        y1 = self.sizes['height'] * 0.25
        y2 = self.sizes['height'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipLeft(self, t=1000, n=1):
        """向左滑动屏幕"""
        x1 = self.sizes['width'] * 0.85
        y1 = self.sizes['height'] * 0.5
        x2 = self.sizes['width'] * 0.15
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipRight(self, t=1000, n=1):
        """向右滑动屏幕"""
        x1 = self.sizes['width'] * 0.25
        y1 = self.sizes['height'] * 0.5
        x2 = self.sizes['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)
