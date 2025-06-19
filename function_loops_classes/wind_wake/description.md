#### 🎯 Task

Assume wind with uniform wind speed $u_0 = 9\ \text{m/s}$ is hitting a $6\ \text{MW}$ wind turbine with rotor diameter
$D = 154\ \text{m}$, located at coordinate $x = 0$. For this wind speed the thrust coefficient below is $c_t = 0.763$.

According to the paper [1], the wind speed $u$ at a distance $x$ behind the turbine can be modelled as

$$ u(x) = u_0 \times \sqrt{1 - \left(\frac{c_t}{8}\right) \left( \frac{D}{\sigma(x)} \right)^2} $$

$$ \sigma(x) = kx + \frac{\sqrt{\beta}D}{4} $$

$$ \beta = \frac{1 + \sqrt{1 - c_t}}{2 \sqrt{1 - c_t}} $$

$$ k = 0.02 $$


**After how many meters behind the rotor has the wind speed recovered to at least $8.95 m/s?**
Define functions **sigma(x)** and **u(x)** *and find out by increasing $x$ in a loop using the formulas above. Save the result in a variable called **recovery_distance**.

#### 🔒 Restrictions

* **Do not use any external libraries** 
* Follow the exact naming (`sigma(x)`, `u(x)`, `recovery_distance`).

**References**<br>
[1] M. Bastankhah and F. Porté-Agel. A new analytical model for wind-turbine wakes. Renewable Energy, 70:116–123, 2014.