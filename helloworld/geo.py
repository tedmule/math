from manim import *

class RectangleWithDiagonal(Scene):
    def construct(self):
        # 创建矩形 ABFE
        rect = Rectangle(width=2, height=1)
        rect.shift(LEFT * 0.5)  # 调整位置
        rect_label = Text("ABFE").next_to(rect, UP)

        # 定义点 A, B, F, E 的坐标
        a = rect.get_top_left()  # A
        b = rect.get_top_right()  # B
        f = rect.get_bottom_right()  # F
        e = rect.get_bottom_left()  # E

        # 定义点 C 和 D
        c = f + RIGHT * 1  # C 在 F 右侧
        d = rect.get_center()  # D 是矩形中心

        # 绘制对角线 AC
        diagonal = Line(a, c)
        
        # 阴影区域（假设是三角形 ACG 或其他）
        shaded_region = Polygon(a, d, c, fill_opacity=0.5, fill_color=GRAY)

        # 标记点
        labels = [
            Tex("A").next_to(a, UP + LEFT),
            Tex("B").next_to(b, UP + RIGHT),
            Tex("F").next_to(f, DOWN + RIGHT),
            Tex("E").next_to(e, DOWN + LEFT),
            Tex("C").next_to(c, DOWN + RIGHT),
            Tex("D").next_to(d, DOWN),
            Tex("G").next_to(d, LEFT),  # G 假设在对角线上靠近 D
        ]

        # 添加到场景
        self.add(rect, diagonal, shaded_region)
        self.add(*labels)

        # 确保所有元素可见
        self.wait(1)

# 运行脚本
if __name__ == "__main__":
    scene = RectangleWithDiagonal()
    scene.render()