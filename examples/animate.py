"""
Tutorial:
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/animate

Usage:
    python3 examples/animate.py > examples/animate.svg
    chromium examples/animate.svg
"""
import svgink as svg


def draw() -> svg.SVG:
    return svg.SVG(
        x=0, y=0,
        width=100, height=100,
        elements=[svg.Rect(
            x=0, y=0,
            width=100, height=100,
            elements=[svg.Animate(
                attributeName="rx",
                values="0;50;0",
                dur="10s",
                repeatCount="indefinite")]
        )]
    )


if __name__ == '__main__':
    print(draw())
