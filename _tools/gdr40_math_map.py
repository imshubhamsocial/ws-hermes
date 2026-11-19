"""GDR40 Math and Diagram Mapping Module."""

DIAGRAM_MAP = {
    "![][image1]": "![GDR40 9-Phase Sequential Execution Pipeline](images/image1.png)",
    "![][image2]": "![Hardware Offload Reserves 5,800 MiB on the RTX 3050](images/image2.png)",
    "![][image55]": "![Native ICM Auditors and SkillEvaluator Tier 1](images/image55.png)"
}

MATH_MAP = {
    "![][image3]": "$h(x, y, t)$", "![][image4]": "$(x, y) \\in [-1, 1]^2$",
    "![][image5]": "$S(x, y, t)$",
    "![][image6]": "$$\\frac{\\partial^2 h}{\\partial t^2} + \\gamma \\frac{\\partial h}{\\partial t} = c^2 \\left( \\frac{\\partial^2 h}{\\partial x^2} + \\frac{\\partial^2 h}{\\partial y^2} \\right) + S(x, y, t)$$",
    "![][image7]": "$256 \\times 256$", "![][image8]": "$\\Delta x = \\Delta y$",
    "![][image9]": "$(i, j)$", "![][image10]": "$n$",
    "![][image11]": "$$\\nabla_d^2 h_{i,j}^n = \\frac{h_{i+1,j}^n + h_{i-1,j}^n + h_{i,j+1}^n + h_{i,j-1}^n - 4h_{i,j}^n}{\\Delta x^2}$$",
    "![][image12]": "$h_{i,j}^n$", "![][image13]": "$h_{i,j}^{n-1}$",
    "![][image14]": "$$h_{i,j}^{n+1} = (2 - \\gamma \\Delta t) h_{i,j}^n - (1 - \\gamma \\Delta t) h_{i,j}^{n-1} + \\text{CFL}^2 \\left( h_{i+1,j}^n + h_{i-1,j}^n + h_{i,j+1}^n + h_{i,j-1}^n - 4h_{i,j}^n \\right)$$",
    "![][image15]": "$\\text{CFL}$", "![][image16]": "$\\text{CFL}^2 = 0.22 \\le 0.5$",
    "![][image17]": "$$\\text{CFL} = \\frac{c \\Delta t}{\\Delta x} < \\frac{1}{\\sqrt{2}}$$",
    "![][image18]": "$\\mathbf{n}(x, y)$",
    "![][image19]": "$$\\mathbf{n}(x, y) = \\frac{\\left( -\\frac{\\partial h}{\\partial x}, 1, -\\frac{\\partial h}{\\partial y} \\right)}{\\sqrt{\\left(\\frac{\\partial h}{\\partial x}\\right)^2 + 1 + \\left(\\frac{\\partial h}{\\partial y}\\right)^2}}$$",
    "![][image20]": "$\\mathbf{i}$", "![][image21]": "$\\eta = n_{\\text{air}} / n_{\\text{water}} = 1.0 / 1.333 \\approx 0.7501875$",
    "![][image22]": "$\\mathbf{t}$",
    "![][image23]": "$$\\mathbf{t} = \\eta \\mathbf{i} + \\left( \\eta c_i - \\sqrt{1 - \\eta^2 (1 - c_i^2)} \\right) \\mathbf{n}, \\quad \\eta = \\frac{n_{\\text{air}}}{n_{\\text{water}}} = \\frac{1.0}{1.333}, \\quad c_i = -\\mathbf{n} \\cdot \\mathbf{i}$$",
    "![][image24]": "$\\mathbf{p}_{\\text{surf}} = (x, h(x, y), y)$", "![][image25]": "$y = y_{\\text{floor}} = -1.0$",
    "![][image26]": "$\\mathbf{p}_{\\text{floor}}$", "![][image27]": "$\\mathbf{p}_{\\text{old}}$",
    "![][image28]": "$$\\mathbf{p}_{\\text{floor}} = \\mathbf{p}_{\\text{surf}} + \\left( \\frac{y_{\\text{floor}} - h(x, y)}{t_y} \\right) \\mathbf{t}$$",
    "![][image29]": "$I_{\\text{caustic}}$",
    "![][image30]": "$$I_{\\text{caustic}} = I_0 \\frac{\\left\\| \\frac{\\partial \\mathbf{p}_{\\text{old}}}{\\partial x} \\times \\frac{\\partial \\mathbf{p}_{\\text{old}}}{\\partial y} \\right\\|}{\\left\\| \\frac{\\partial \\mathbf{p}_{\\text{floor}}}{\\partial x} \\times \\frac{\\partial \\mathbf{p}_{\\text{floor}}}{\\partial y} \\right\\| + \\epsilon}$$",
    "![][image31]": "$R$", "![][image32]": "$\\rho_s < \\rho_{\\text{water}}$",
    "![][image33]": "$y_s$", "![][image34]": "$d$", "![][image35]": "$h(x_s, z_s)$", "![][image36]": "$[0, 2R]$",
    "![][image37]": "$$d = \\text{clamp}\\left( h(x_s, z_s) - (y_s - R), 0, 2R \\right)$$",
    "![][image38]": "$V_{\\text{sub}}(d)$",
    "![][image39]": "$$V_{\\text{sub}}(d) = \\frac{\\pi d^2}{3}(3R - d)$$",
    "![][image40]": "$\\mathbf{F}_{\\text{net}}$", "![][image41]": "$m_s = \\frac{4}{3}\\pi R^3 \\rho_s$",
    "![][image42]": "$\\mathbf{v}_{\\text{rel}} = \\mathbf{v}_s - \\mathbf{v}_{\\text{water}}$",
    "![][image43]": "$$\\mathbf{F}_{\\text{net}} = \\rho_{\\text{water}} g V_{\\text{sub}}(d) \\mathbf{e}_y - m_s g \\mathbf{e}_y - \\frac{1}{2}\\rho_{\\text{water}} C_d A_{\\text{sub}}(d) \\|\\mathbf{v}_{\\text{rel}}\\| \\mathbf{v}_{\\text{rel}}$$",
    "![][image44]": "$\\mathbf{v}_s$", "![][image45]": "$\\mathbf{x}_s$",
    "![][image46]": "$$\\mathbf{v}_s^{n+1} = \\mathbf{v}_s^n + \\frac{\\mathbf{F}_{\\text{net}}}{m_s} \\Delta t, \\quad \\mathbf{x}_s^{n+1} = \\mathbf{x}_s^n + \\mathbf{v}_s^{n+1} \\Delta t$$",
    "![][image47]": "$k \\in \\{1, \\dots, N\\}$", "![][image48]": "$\\mathbf{x}_k$",
    "![][image49]": "$\\mathbf{v}_k$", "![][image50]": "$\\mathbf{a}_k$", "![][image51]": "$\\mathbf{a}_{\\text{wall}}(\\mathbf{x}_k)$",
    "![][image52]": "$$\\mathbf{a}_k = w_s \\sum_{j \\in \\mathcal{N}_k} \\frac{\\mathbf{x}_k - \\mathbf{x}_j}{\\|\\mathbf{x}_k - \\mathbf{x}_j\\|^2 + \\epsilon} + w_a (\\bar{\\mathbf{v}}_k - \\mathbf{v}_k) + w_c (\\bar{\\mathbf{x}}_k - \\mathbf{x}_k) + \\mathbf{a}_{\\text{wall}}(\\mathbf{x}_k)$$",
    "![][image53]": "$[v_{\\min}, v_{\\max}]$",
    "![][image54]": "$$\\mathbf{v}_k^{n+1} = \\text{clamp}_{[v_{\\min}, v_{\\max}]}\\left( \\mathbf{v}_k^n + \\mathbf{a}_k \\Delta t \\right), \\quad \\mathbf{x}_k^{n+1} = \\mathbf{x}_k^n + \\mathbf{v}_k^{n+1} \\Delta t$$"
}
