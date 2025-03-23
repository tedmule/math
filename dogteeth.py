from manim import *
import random

class Dog(Scene):
    def construct(self):
        # 定义长方形的四个顶点
        A = [-2, -1, 0]  # 左下角
        B = [2, -1, 0]   # 右下角
        C = [2, 1, 0]    # 右上角
        D = [-2, 1, 0]   # 左上角

        # 创建长方形的线段
        rect = Polygon(A, B, C, D, color=WHITE)
        
        # 添加顶点标签
        label_A = Text("A").next_to(A, DOWN+LEFT, buff=0.1)
        label_B = Text("B").next_to(B, DOWN+RIGHT, buff=0.1)
        label_C = Text("C").next_to(C, UP+RIGHT, buff=0.1)
        label_D = Text("D").next_to(D, UP+LEFT, buff=0.1)

        # 创建初始三角形（顶点从D开始）
        triangle = Polygon(A, B, D, color=BLUE, fill_opacity=0.3)
        
        # 显示长方形和标签
        self.play(Create(rect))
        self.play(
            Write(label_A),
            Write(label_B),
            Write(label_C),
            Write(label_D)
        )
        
        # 添加初始三角形
        self.play(Create(triangle))
        self.wait(1)

        # 创建移动的顶点（从D到C）
        moving_point = Dot(D, color=YELLOW)
        self.add(moving_point)

        # 定义顶点位置的更新函数
        def update_triangle(tri):
            new_pos = moving_point.get_center()
            tri.become(Polygon(A, B, new_pos, color=BLUE, fill_opacity=0.3))

        triangle.add_updater(update_triangle)

        # 创建顶点从D到C的动画
        self.play(
            moving_point.animate.move_to(C),
            run_time=4,
            rate_func=linear
        )

        # 清除更新器并等待
        triangle.clear_updaters()
        self.wait(1)

        # 可选：返回到起点D
        self.play(
            moving_point.animate.move_to(D),
            triangle.animate.become(Polygon(A, B, D, color=BLUE, fill_opacity=0.3)),
            run_time=4,
            rate_func=linear
        )

        self.wait(2)




class Dog1(Scene):
    def construct(self):
        # 定义长方形的四个顶点
        A = [-2, -1, 0]  # 左下角
        B = [2, -1, 0]   # 右下角
        C = [2, 1, 0]    # 右上角
        D = [-2, 1, 0]   # 左上角

        # 创建长方形的线段
        rect = Polygon(A, B, C, D, color=WHITE)
        
        # 添加顶点标签
        label_A = Text("A").next_to(A, DOWN+LEFT, buff=0.1)
        label_B = Text("B").next_to(B, DOWN+RIGHT, buff=0.1)
        label_C = Text("C").next_to(C, UP+RIGHT, buff=0.1)
        label_D = Text("D").next_to(D, UP+LEFT, buff=0.1)

        # 创建初始三角形（顶点在左中点）
        start_point = [-2, 0, 0]  # 面积平分线上的起点
        triangle = Polygon(A, B, start_point, color=BLUE, fill_opacity=0.3)
        
        # 显示长方形和标签
        self.play(Create(rect))
        self.play(
            Write(label_A),
            Write(label_B),
            Write(label_C),
            Write(label_D)
        )
        
        # 添加初始三角形
        self.play(Create(triangle))
        self.wait(1)

        # 创建移动的顶点（从左到右）
        moving_point = Dot(start_point, color=YELLOW)
        self.add(moving_point)

        # 添加面积平分线（可选，用于可视化）
        midline = Line([-2, 0, 0], [2, 0, 0], color=GRAY, stroke_width=1)
        self.play(Create(midline))
        
        # 定义顶点位置的更新函数
        def update_triangle(tri):
            new_pos = moving_point.get_center()
            tri.become(Polygon(A, B, new_pos, color=BLUE, fill_opacity=0.3))

        triangle.add_updater(update_triangle)

        # 创建顶点沿中线从左到右的动画
        end_point = [2, 0, 0]  # 面积平分线上的终点
        self.play(
            moving_point.animate.move_to(end_point),
            run_time=4,
            rate_func=linear
        )

        # 清除更新器并等待
        triangle.clear_updaters()
        self.wait(1)

        # 返回到起点
        self.play(
            moving_point.animate.move_to(start_point),
            triangle.animate.become(Polygon(A, B, start_point, color=BLUE, fill_opacity=0.3)),
            run_time=4,
            rate_func=linear
        )

        self.wait(2)



class Dog2(Scene):
    def construct(self):
        # 定义长方形的四个顶点
        A = [-2, -1, 0]  # 左下角
        B = [2, -1, 0]   # 右下角
        C = [2, 1, 0]    # 右上角
        D = [-2, 1, 0]   # 左上角

        # 创建长方形的线段
        rect = Polygon(A, B, C, D, color=WHITE)
        
        # 添加顶点标签
        label_A = Text("A").next_to(A, DOWN+LEFT, buff=0.1)
        label_B = Text("B").next_to(B, DOWN+RIGHT, buff=0.1)
        label_C = Text("C").next_to(C, UP+RIGHT, buff=0.1)
        label_D = Text("D").next_to(D, UP+LEFT, buff=0.1)

        # 定义两个三角形的初始顶点（沿中线）
        start_point = [-2, 0, 0]  # 中线起点
        tri1 = Polygon(A, start_point, D, color=BLUE, fill_opacity=0.3)  # 以A为底顶点
        tri2 = Polygon(B, start_point, C, color=GREEN, fill_opacity=0.3) # 以B为底顶点
        
        # 显示长方形和标签
        self.play(Create(rect))
        self.play(
            Write(label_A),
            Write(label_B),
            Write(label_C),
            Write(label_D)
        )
        
        # 添加两个初始三角形
        self.play(Create(tri1), Create(tri2))
        self.wait(1)

        # 创建移动的顶点
        moving_point = Dot(start_point, color=YELLOW)
        self.add(moving_point)

        # 添加面积平分线（可选）
        midline = Line([-2, 0, 0], [2, 0, 0], color=GRAY, stroke_width=1)
        self.play(Create(midline))
        
        # 定义两个三角形的更新函数
        def update_tri1(tri):
            new_pos = moving_point.get_center()
            tri.become(Polygon(A, new_pos, D, color=BLUE, fill_opacity=0.3))

        def update_tri2(tri):
            new_pos = moving_point.get_center()
            tri.become(Polygon(B, new_pos, C, color=GREEN, fill_opacity=0.3))

        tri1.add_updater(update_tri1)
        tri2.add_updater(update_tri2)

        # 创建顶点沿中线从左到右的动画
        end_point = [2, 0, 0]  # 中线终点
        self.play(
            moving_point.animate.move_to(end_point),
            run_time=4,
            rate_func=linear
        )

        # 清除更新器并等待
        tri1.clear_updaters()
        tri2.clear_updaters()
        self.wait(1)

        # 返回到起点
        self.play(
            moving_point.animate.move_to(start_point),
            tri1.animate.become(Polygon(A, start_point, D, color=BLUE, fill_opacity=0.3)),
            tri2.animate.become(Polygon(B, start_point, C, color=GREEN, fill_opacity=0.3)),
            run_time=4,
            rate_func=linear
        )

        self.wait(2)



class Dog3(Scene):
    def construct(self):
        # 定义长方形的四个顶点
        A = [-2, -1, 0]  # 左下角
        B = [2, -1, 0]   # 右下角
        C = [2, 1, 0]    # 右上角
        D = [-2, 1, 0]   # 左上角

        # 计算AB的中点M
        M = [0, -1, 0]  # AB的中点

        # 创建长方形的线段
        rect = Polygon(A, B, C, D, color=WHITE)
        
        # 添加顶点标签
        label_A = Text("A").next_to(A, DOWN+LEFT, buff=0.1)
        label_B = Text("B").next_to(B, DOWN+RIGHT, buff=0.1)
        label_C = Text("C").next_to(C, UP+RIGHT, buff=0.1)
        label_D = Text("D").next_to(D, UP+LEFT, buff=0.1)
        label_M = Text("M").next_to(M, DOWN, buff=0.1)

        # 定义两个三角形的初始顶点（沿中线）
        start_point = [-2, 0, 0]  # 中线起点
        tri1 = Polygon(A, M, start_point, color=BLUE, fill_opacity=0.3)  # 三角形AM+移动点
        tri2 = Polygon(M, B, start_point, color=GREEN, fill_opacity=0.3) # 三角形MB+移动点
        
        # 显示长方形和标签
        self.play(Create(rect))
        self.play(
            Write(label_A),
            Write(label_B),
            Write(label_C),
            Write(label_D),
            Write(label_M)
        )
        
        # 添加两个初始三角形
        self.play(Create(tri1), Create(tri2))
        self.wait(1)

        # 创建移动的顶点
        moving_point = Dot(start_point, color=YELLOW)
        self.add(moving_point)

        # 添加面积平分线（可选）
        midline = Line([-2, 0, 0], [2, 0, 0], color=GRAY, stroke_width=1)
        self.play(Create(midline))
        
        # 定义两个三角形的更新函数
        def update_tri1(tri):
            new_pos = moving_point.get_center()
            tri.become(Polygon(A, M, new_pos, color=BLUE, fill_opacity=0.3))

        def update_tri2(tri):
            new_pos = moving_point.get_center()
            tri.become(Polygon(M, B, new_pos, color=GREEN, fill_opacity=0.3))

        tri1.add_updater(update_tri1)
        tri2.add_updater(update_tri2)

        # 创建顶点沿中线从左到右的动画
        end_point = [2, 0, 0]  # 中线终点
        self.play(
            moving_point.animate.move_to(end_point),
            run_time=4,
            rate_func=linear
        )

        # 清除更新器并等待
        tri1.clear_updaters()
        tri2.clear_updaters()
        self.wait(1)

        # 返回到起点
        self.play(
            moving_point.animate.move_to(start_point),
            tri1.animate.become(Polygon(A, M, start_point, color=BLUE, fill_opacity=0.3)),
            tri2.animate.become(Polygon(M, B, start_point, color=GREEN, fill_opacity=0.3)),
            run_time=4,
            rate_func=linear
        )

        self.wait(2)


class Dog4(Scene):
    def construct(self):
        # 定义长方形的四个顶点
        A = [-2, -1, 0]  # 左下角
        B = [2, -1, 0]   # 右下角
        C = [2, 1, 0]    # 右上角
        D = [-2, 1, 0]   # 左上角

        # 计算AB的中点M
        M = [0, -1, 0]  # AB的中点

        # 创建长方形的线段
        rect = Polygon(A, B, C, D, color=WHITE)
        
        # 添加顶点标签
        label_A = Text("A").next_to(A, DOWN+LEFT, buff=0.1)
        label_B = Text("B").next_to(B, DOWN+RIGHT, buff=0.1)
        label_C = Text("C").next_to(C, UP+RIGHT, buff=0.1)
        label_D = Text("D").next_to(D, UP+LEFT, buff=0.1)
        label_M = Text("M").next_to(M, DOWN, buff=0.1)

        # 随机生成两个三角形顶点的初始位置（在y=0的中线上，x在-2到2之间）
        start_point1 = [random.uniform(-2, 2), 0, 0]  # 第一个三角形的初始顶点
        start_point2 = [random.uniform(-2, 2), 0, 0]  # 第二个三角形的初始顶点

        # 定义两个三角形
        tri1 = Polygon(A, M, start_point1, color=BLUE, fill_opacity=0.3)  # 三角形AM+移动点1
        tri2 = Polygon(M, B, start_point2, color=GREEN, fill_opacity=0.3) # 三角形MB+移动点2
        
        # 显示长方形和标签
        self.play(Create(rect))
        self.play(
            Write(label_A),
            Write(label_B),
            Write(label_C),
            Write(label_D),
            Write(label_M)
        )
        
        # 添加两个初始三角形
        self.play(Create(tri1), Create(tri2))
        self.wait(1)

        # 创建两个移动的顶点
        moving_point1 = Dot(start_point1, color=YELLOW)
        moving_point2 = Dot(start_point2, color=WHITE)
        self.add(moving_point1, moving_point2)

        # 添加面积平分线（可选）
        midline = Line([-2, 0, 0], [2, 0, 0], color=GRAY, stroke_width=1)
        self.play(Create(midline))
        
        # 定义两个三角形的更新函数
        def update_tri1(tri):
            new_pos = moving_point1.get_center()
            tri.become(Polygon(A, M, new_pos, color=BLUE, fill_opacity=0.3))

        def update_tri2(tri):
            new_pos = moving_point2.get_center()
            tri.become(Polygon(M, B, new_pos, color=GREEN, fill_opacity=0.3))

        tri1.add_updater(update_tri1)
        tri2.add_updater(update_tri2)

        # 创建顶点沿中线向右移动的动画（都移动到x=2）
        end_point = [2, 0, 0]  # 目标点
        self.play(
            moving_point1.animate.move_to(end_point),
            moving_point2.animate.move_to(end_point),
            run_time=4,
            rate_func=linear
        )

        # 清除更新器并等待
        tri1.clear_updaters()
        tri2.clear_updaters()
        self.wait(1)

        # 返回到各自的初始位置
        self.play(
            moving_point1.animate.move_to(start_point1),
            moving_point2.animate.move_to(start_point2),
            tri1.animate.become(Polygon(A, M, start_point1, color=BLUE, fill_opacity=0.3)),
            tri2.animate.become(Polygon(M, B, start_point2, color=GREEN, fill_opacity=0.3)),
            run_time=4,
            rate_func=linear
        )

        self.wait(2)



class Dog5(Scene):
    def construct(self):
        # 定义长方形的四个顶点
        A = [-2, -1, 0]  # 左下角
        B = [2, -1, 0]   # 右下角
        C = [2, 1, 0]    # 右上角
        D = [-2, 1, 0]   # 左上角

        # 计算下半部分底边AB的中点M
        M = [0, -1, 0]  # AB的中点

        # 计算上半部分底边CD的分割点（3等份）
        P1 = [-2/3, 1, 0]  # CD的1/3处
        P2 = [2/3, 1, 0]   # CD的2/3处

        # 创建长方形的线段
        rect = Polygon(A, B, C, D, color=WHITE)
        
        # 添加顶点标签
        label_A = Text("A").next_to(A, DOWN+LEFT, buff=0.1)
        label_B = Text("B").next_to(B, DOWN+RIGHT, buff=0.1)
        label_C = Text("C").next_to(C, UP+RIGHT, buff=0.1)
        label_D = Text("D").next_to(D, UP+LEFT, buff=0.1)
        label_M = Text("M").next_to(M, DOWN, buff=0.1)
        label_P1 = Text("P1").next_to(P1, UP, buff=0.1)
        label_P2 = Text("P2").next_to(P2, UP, buff=0.1)

        # 下半部分两个三角形的随机初始顶点（y=0）
        # start_point1 = [random.uniform(-2, 2), 0, 0]  # 第一个三角形（AM）
        # start_point2 = [random.uniform(-2, 2), 0, 0]  # 第二个三角形（MB）
        start_point1 = [-1, 0, 0]  # 第一个三角形（AM）
        start_point2 = [0, 0, 0]  # 第二个三角形（MB）

        # 上半部分三个三角形的随机初始顶点（y=0）
        # start_point3 = [random.uniform(-2, 2), 0, 0]  # 第三个三角形（DP1）
        # start_point4 = [random.uniform(-2, 2), 0, 0]  # 第四个三角形（P1P2）
        # start_point5 = [random.uniform(-2, 2), 0, 0]  # 第五个三角形（P2C）
        start_point3 = [random.uniform(-1.5, 2), 0, 0]  # 第三个三角形（DP1）
        start_point4 = [random.uniform(-0.5, 2), 0, 0]  # 第四个三角形（P1P2）
        start_point5 = [random.uniform(1, 2), 0, 0]  # 第五个三角形（P2C）

        # 定义下半部分的两个三角形
        tri1 = Polygon(A, M, start_point1, color=BLUE, fill_opacity=0.3)    # AM+移动点1
        tri2 = Polygon(M, B, start_point2, color=GREEN, fill_opacity=0.3)   # MB+移动点2

        # 定义上半部分的三个三角形
        tri3 = Polygon(D, P1, start_point3, color=RED, fill_opacity=0.3)    # DP1+移动点3
        tri4 = Polygon(P1, P2, start_point4, color=YELLOW, fill_opacity=0.3) # P1P2+移动点4
        tri5 = Polygon(P2, C, start_point5, color=PURPLE, fill_opacity=0.3) # P2C+移动点5
        
        # 显示长方形和标签
        self.play(Create(rect))
        self.play(
            Write(label_A), Write(label_B), Write(label_C), Write(label_D),
            Write(label_M), Write(label_P1), Write(label_P2)
        )
        
        # 添加所有初始三角形
        self.play(Create(tri1), Create(tri2), Create(tri3), Create(tri4), Create(tri5))
        self.wait(5)

        # 创建五个移动的顶点
        moving_point1 = Dot(start_point1, color=YELLOW)
        moving_point2 = Dot(start_point2, color=WHITE)
        moving_point3 = Dot(start_point3, color=RED)
        moving_point4 = Dot(start_point4, color=GREEN)
        moving_point5 = Dot(start_point5, color=BLUE)
        self.add(moving_point1, moving_point2, moving_point3, moving_point4, moving_point5)

        # 添加面积平分线（y=0）
        midline = Line([-2, 0, 0], [2, 0, 0], color=GRAY, stroke_width=1)
        self.play(Create(midline))
        
        # 定义五个三角形的更新函数
        def update_tri1(tri):
            new_pos = moving_point1.get_center()
            tri.become(Polygon(A, M, new_pos, color=BLUE, fill_opacity=0.3))

        def update_tri2(tri):
            new_pos = moving_point2.get_center()
            tri.become(Polygon(M, B, new_pos, color=GREEN, fill_opacity=0.3))

        def update_tri3(tri):
            new_pos = moving_point3.get_center()
            tri.become(Polygon(D, P1, new_pos, color=RED, fill_opacity=0.3))

        def update_tri4(tri):
            new_pos = moving_point4.get_center()
            tri.become(Polygon(P1, P2, new_pos, color=YELLOW, fill_opacity=0.3))

        def update_tri5(tri):
            new_pos = moving_point5.get_center()
            tri.become(Polygon(P2, C, new_pos, color=PURPLE, fill_opacity=0.3))

        tri1.add_updater(update_tri1)
        tri2.add_updater(update_tri2)
        tri3.add_updater(update_tri3)
        tri4.add_updater(update_tri4)
        tri5.add_updater(update_tri5)

        # 创建所有顶点向右移动的动画（到x=2）
        end_point = [2, 0, 0]
        self.play(
            moving_point1.animate.move_to(end_point),
            moving_point2.animate.move_to(end_point),
            moving_point3.animate.move_to(end_point),
            moving_point4.animate.move_to(end_point),
            moving_point5.animate.move_to(end_point),
            run_time=4,
            rate_func=linear
        )

        # 清除更新器并等待
        tri1.clear_updaters()
        tri2.clear_updaters()
        tri3.clear_updaters()
        tri4.clear_updaters()
        tri5.clear_updaters()
        self.wait(5)

        # # 返回到各自的初始位置
        # self.play(
        #     moving_point1.animate.move_to(start_point1),
        #     moving_point2.animate.move_to(start_point2),
        #     moving_point3.animate.move_to(start_point3),
        #     moving_point4.animate.move_to(start_point4),
        #     moving_point5.animate.move_to(start_point5),
        #     tri1.animate.become(Polygon(A, M, start_point1, color=BLUE, fill_opacity=0.3)),
        #     tri2.animate.become(Polygon(M, B, start_point2, color=GREEN, fill_opacity=0.3)),
        #     tri3.animate.become(Polygon(D, P1, start_point3, color=RED, fill_opacity=0.3)),
        #     tri4.animate.become(Polygon(P1, P2, start_point4, color=YELLOW, fill_opacity=0.3)),
        #     tri5.animate.become(Polygon(P2, C, start_point5, color=PURPLE, fill_opacity=0.3)),
        #     run_time=4,
        #     rate_func=linear
        # )

        # self.wait(5)


class Dog6(Scene):
    def construct(self):
        # 定义长方形的四个顶点
        A = [-2, -1, 0]  # 左下角
        B = [2, -1, 0]   # 右下角
        C = [2, 1, 0]    # 右上角
        D = [-2, 1, 0]   # 左上角

        # 计算下半部分底边AB的中点M
        M = [0, -1, 0]  # AB的中点

        # 不等分上半部分底边CD（按1:2:1比例分割）
        P1 = [-1, 1, 0]  # CD的1/4处（-2到-1）
        P2 = [1, 1, 0]   # CD的3/4处（-1到2之间的1）

        # 创建长方形的线段
        rect = Polygon(A, B, C, D, color=WHITE)
        
        # 添加顶点标签
        label_A = Text("A").next_to(A, DOWN+LEFT, buff=0.1)
        label_B = Text("B").next_to(B, DOWN+RIGHT, buff=0.1)
        label_C = Text("C").next_to(C, UP+RIGHT, buff=0.1)
        label_D = Text("D").next_to(D, UP+LEFT, buff=0.1)
        label_M = Text("M").next_to(M, DOWN, buff=0.1)
        label_P1 = Text("P1").next_to(P1, UP, buff=0.1)
        label_P2 = Text("P2").next_to(P2, UP, buff=0.1)

        # 下半部分两个三角形的随机初始顶点（y=0）
        # start_point1 = [random.uniform(-2, 2), 0, 0]  # 第一个三角形（AM）
        # start_point2 = [random.uniform(-2, 2), 0, 0]  # 第二个三角形（MB）
        start_point1 = [-1, 0, 0]  # 第一个三角形（AM）
        start_point2 = [1.4, 0, 0]  # 第二个三角形（MB）

        # 上半部分三个三角形的随机初始顶点（y=0）
        # start_point3 = [random.uniform(-2, 2), 0, 0]  # 第三个三角形（DP1）
        # start_point4 = [random.uniform(-2, 2), 0, 0]  # 第四个三角形（P1P2）
        # start_point5 = [random.uniform(-2, 2), 0, 0]  # 第五个三角形（P2C）
        start_point3 = [-1.8, 0, 0]  # 第三个三角形（DP1）
        start_point4 = [0, 0, 0]  # 第四个三角形（P1P2）
        start_point5 = [1.6, 0, 0]  # 第五个三角形（P2C）

        # 定义下半部分的两个三角形
        tri1 = Polygon(A, M, start_point1, color=BLUE, fill_opacity=0.3)    # AM+移动点1
        tri2 = Polygon(M, B, start_point2, color=GREEN, fill_opacity=0.3)   # MB+移动点2

        # 定义上半部分的三个三角形
        tri3 = Polygon(D, P1, start_point3, color=RED, fill_opacity=0.3)    # DP1+移动点3
        tri4 = Polygon(P1, P2, start_point4, color=YELLOW, fill_opacity=0.3) # P1P2+移动点4
        tri5 = Polygon(P2, C, start_point5, color=PURPLE, fill_opacity=0.3) # P2C+移动点5
        
        # 显示长方形和标签
        self.play(Create(rect))
        self.play(
            Write(label_A), Write(label_B), Write(label_C), Write(label_D),
            Write(label_M), Write(label_P1), Write(label_P2)
        )
        
        # 添加所有初始三角形
        self.play(Create(tri1), Create(tri2), Create(tri3), Create(tri4), Create(tri5))
        self.wait(1)

        # 创建五个移动的顶点
        moving_point1 = Dot(start_point1, color=YELLOW)
        moving_point2 = Dot(start_point2, color=WHITE)
        moving_point3 = Dot(start_point3, color=RED)
        moving_point4 = Dot(start_point4, color=GREEN)
        moving_point5 = Dot(start_point5, color=BLUE)
        self.add(moving_point1, moving_point2, moving_point3, moving_point4, moving_point5)

        # 添加面积平分线（y=0），并明确显示
        midline = Line([-2, 0, 0], [2, 0, 0], color=ORANGE, stroke_width=3)
        midline_label = Text("").next_to(midline, UP, buff=0.1).scale(0.7)
        self.play(Create(midline), Write(midline_label))
        
        # 定义五个三角形的更新函数
        def update_tri1(tri):
            new_pos = moving_point1.get_center()
            tri.become(Polygon(A, M, new_pos, color=BLUE, fill_opacity=0.3))

        def update_tri2(tri):
            new_pos = moving_point2.get_center()
            tri.become(Polygon(M, B, new_pos, color=GREEN, fill_opacity=0.3))

        def update_tri3(tri):
            new_pos = moving_point3.get_center()
            tri.become(Polygon(D, P1, new_pos, color=RED, fill_opacity=0.3))

        def update_tri4(tri):
            new_pos = moving_point4.get_center()
            tri.become(Polygon(P1, P2, new_pos, color=YELLOW, fill_opacity=0.3))

        def update_tri5(tri):
            new_pos = moving_point5.get_center()
            tri.become(Polygon(P2, C, new_pos, color=PURPLE, fill_opacity=0.3))

        tri1.add_updater(update_tri1)
        tri2.add_updater(update_tri2)
        tri3.add_updater(update_tri3)
        tri4.add_updater(update_tri4)
        tri5.add_updater(update_tri5)

        # 创建所有顶点向右移动的动画（到x=2）
        end_point = [2, 0, 0]
        self.play(
            moving_point1.animate.move_to(end_point),
            moving_point2.animate.move_to(end_point),
            moving_point3.animate.move_to(end_point),
            moving_point4.animate.move_to(end_point),
            moving_point5.animate.move_to(end_point),
            run_time=4,
            rate_func=linear
        )

        # 清除更新器并等待
        tri1.clear_updaters()
        tri2.clear_updaters()
        tri3.clear_updaters()
        tri4.clear_updaters()
        tri5.clear_updaters()
        self.wait(2)

        # 返回到各自的初始位置
        # self.play(
        #     moving_point1.animate.move_to(start_point1),
        #     moving_point2.animate.move_to(start_point2),
        #     moving_point3.animate.move_to(start_point3),
        #     moving_point4.animate.move_to(start_point4),
        #     moving_point5.animate.move_to(start_point5),
        #     tri1.animate.become(Polygon(A, M, start_point1, color=BLUE, fill_opacity=0.3)),
        #     tri2.animate.become(Polygon(M, B, start_point2, color=GREEN, fill_opacity=0.3)),
        #     tri3.animate.become(Polygon(D, P1, start_point3, color=RED, fill_opacity=0.3)),
        #     tri4.animate.become(Polygon(P1, P2, start_point4, color=YELLOW, fill_opacity=0.3)),
        #     tri5.animate.become(Polygon(P2, C, start_point5, color=PURPLE, fill_opacity=0.3)),
        #     run_time=4,
        #     rate_func=linear
        # )

        # self.wait(2)
