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

- Beta v0.4

Implemented in prototype:

- Home page
- Recipe library page
- Updated category structure: Baking / Drinks / Oven Dishes
- Drink second-level filters: Coffee, Matcha/Tea, Cocoa/Milk Drinks
- Coffee method filters: Pour-over, Espresso, Milk Coffee, Cold Brew
- Recipe cards exposing difficulty, time, tools, and key risk
- Banana Blueberry Muffin detail page sample
- Editable Swiss Roll detail page with classic, sugar-free/oil-free, and cocoa variants
- Shared recipe schema with category extensions
- Editable Pour-over Coffee detail page with drink-specific parameters and key-state process images
- Local recipe creator with Baking and Drink starter templates
- Custom recipe cards, editable parameters/steps/states/troubleshooting, compressed cover and step images, and JSON backup
- Category-aware parameter editing for custom recipes, with Baking/Drink presets, custom labels, and button-based ordering
- Local note-to-recipe import with numbered-step parsing and a confirmation preview
- Reusable coffee bean profiles linked to dedicated pour-over and semi-automatic espresso recipe templates
- A dedicated Coffee Bean Library navigation module with repeatable variety/process/blend-ratio rows
- Coffee bean detail pages with linked brewing recipes and bean-aware shortcuts for creating pour-over or espresso methods
- A full-height coffee bean editor with a scrollable field area and always-visible save actions on mobile and desktop
- A dedicated pour-over plan editor organized by start time, cumulative water, pouring technique, and result notes
- Full-device backup and restore for all Brew & Bake Lab browser data
- Installable PWA with synchronized updates, a timed offline fallback, and lightweight runtime image caching for unstable mobile networks
- Shared follow-along mode for Swiss Roll, Pour-over Coffee, and custom recipes, with per-recipe progress and screen wake lock where supported
- Before-start checklist
- Parameter card
- Step cards
- Key state placeholders
- Troubleshooting
- Follow-along mode

## Current Schema Direction

Use one shared recipe skeleton with category-specific extensions:

- Shared: overview, ingredients and tools, parameters, steps, key states, troubleshooting, versions
- Baking: oven and pan, baking, shaping and setting
- Drinks: ratio, water temperature, grind size, pouring rhythm

Swiss Roll and Pour-over Coffee are the first two validation recipes.

## Planned Work

Complete the general recipe workflow before expanding the template system:

1. Refine structured ingredients, tools, and category-specific parameters.
2. Add faster import from personal notes.
3. Design reusable recipe templates.

The coffee templates should separate reusable bean information from brewing recipes:

- Coffee bean profile: roaster, origin, variety, process, roast level, roast date, tasting notes, and recommended resting period.
- Pour-over recipe: preparation parameters, an automatically derived ratio, pouring stages (start time, cumulative water, and technique), total time, and result notes.
- Semi-automatic espresso recipe: bean dose, yield, ratio, grind setting, extraction time, temperature, pressure when relevant, basket, milk parameters, and result notes.
- One coffee bean profile can link to multiple pour-over or espresso recipes so the bean information does not need to be entered repeatedly.
