# Brew & Bake Lab Project Brief

## Positioning

Brew & Bake Lab is a public-facing practical guide for drinks, baking, and oven dishes.

The product should feel like a parameterized kitchen manual rather than a recipe blog. Each work should help users prepare, execute, judge state, and troubleshoot while they are actively making something.

## Core Principle

Users should know all required materials, tools, prep work, parameters, and risks before starting a step.

Each recipe/work should include:

- Ingredients and tools, separated clearly
- Estimated total time and active time
- Parameters such as temperature, time, ratio, mold size, quantity, and state cues
- Concise step-by-step workflow
- Per-step required items, actions, judgment criteria, and cautions
- Images, diagrams, or GIFs for state and technique
- Troubleshooting table
- Version notes for future iterations

## Information Architecture

Primary navigation:

- Home
- Recipe Library
- Technique Library
- Parameter Notes

Home primary categories:

- Baking
- Drinks
- Oven Dishes

Technique Library is not treated as a "what to make" category. It remains a standalone learning section and is also referenced inside category pages and recipe steps.

## Drinks Taxonomy

Drinks should contain multiple second-level categories instead of being limited to coffee.

- Drinks
  - Coffee
    - Pour-over
    - Espresso
    - Milk coffee
    - Cold brew
    - Moka pot
    - French press
  - Matcha / Tea
    - Matcha latte
    - Iced matcha
    - Milk tea
    - Cold-brew tea
  - Cocoa / Milk Drinks
    - Hot cocoa
    - Chocolate milk
    - Vanilla milk

## First Batch Of Works

- Banana Blueberry Muffins
- Swiss Roll
- Naked Cake
- Roasted Chicken Wings
- Pour-over Coffee

## Recipe Detail Template

Each detail page should contain:

1. Overview
   - Title
   - Category
   - Difficulty
   - Yield
   - Total time
   - Active time
   - Key equipment
   - Success keys

2. Before-Start Checklist
   - Ingredients
   - Tools
   - Prep work
   - Cannot-miss items

3. Parameter Cards
   - Temperature
   - Time
   - Mold/container/tool
   - Quantity
   - Critical state cues

4. Step Flow
   Each step includes:
   - Required items
   - Action
   - Visual or tactile judgment
   - Caution
   - Image/diagram/GIF placeholder

5. Key State Gallery
   Examples:
   - Egg white peaks
   - Batter texture
   - Cream whipping states
   - Coffee bed state
   - Chicken wing browning

6. Troubleshooting
   - Problem
   - Possible cause
   - Next adjustment

7. Version Notes
   Example:
   - v1 regular sugar
   - v2 reduced sugar
   - v3 more fruit

## Prototype

Current prototype file:

- `/Users/toya/Documents/Brew-Bake-Lab/index.html`

Current prototype version shown in UI:

- Prototype v0.3

Implemented in prototype:

- Home page
- Recipe library page
- Updated category structure: Baking / Drinks / Oven Dishes
- Drink second-level filters: Coffee, Matcha/Tea, Cocoa/Milk Drinks
- Coffee method filters: Pour-over, Espresso, Milk Coffee, Cold Brew
- Recipe cards exposing difficulty, time, tools, and key risk
- Banana Blueberry Muffin detail page sample
- Before-start checklist
- Parameter card
- Step cards
- Key state placeholders
- Troubleshooting
- Follow-along mode placeholder

## Next Design Step

Build the Swiss Roll detail page to test a more complex workflow:

- Egg white peak state
- Cake roll batter mixing
- Oven temperature tuning
- Surface cracking
- Pre-roll and chilling
- Cream filling
- Troubleshooting for cracking, wet center, shrinkage, and rough texture
