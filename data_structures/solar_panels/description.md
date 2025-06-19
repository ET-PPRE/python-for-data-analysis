#### 🎯 Task

You are given the daily energy output (in kWh) of three different solar panels over a week and have to calculate the enegery that has been generated during this time. 

- Create a dictionary called `panel_output`, where each **key** is called `Panel1`, `Panel2` and `Panel3`, which have generated the following energy for the week we are analyzing:

    **Panel1**: [23, 25, 28, 21, 26, 27, 25]
    **Panel2**: [24, -9999, 27, 26, -88888, 29, 26]
    **Panel3**: [20, 22, 23, 21, 24, 25, 22]
- The values -9999 and -88888 in 'Panel2' indicate erroneous readings. Before performing any calculation you should replace all values less than zero in 'Panel2' with `0`, save the modified dictionary as a new variable called `panel_output_cleaned`.
- Write a function called `weekly_production`, that takes the **list** of the seven daily measurements of the solar panels and **returns** the total output over the week. Create a loop to use your function to print each panel’s label and its total weekly output.
- Determine the panel with the highest total output and save its label as `most_produced`, print the name of the panel and the total value.

#### 🔒 Restrictions

* **Do not use any external libraries**.
* Follow the exact naming (`panel_output`, `Panel1`, `Panel2`, `Panel3`, `panel_output_cleaned`, `weekly_production`, `most_produced`).