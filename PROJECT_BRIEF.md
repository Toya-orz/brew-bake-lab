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
- Local TXT and Markdown note-file loading into the recipe parser, with file-size and content-length guards
- Reusable coffee bean profiles linked to dedicated pour-over and semi-automatic espresso recipe templates
- A dedicated Coffee Bean Library navigation module with repeatable variety/process/blend-ratio rows
- Coffee bean detail pages with linked brewing recipes and bean-aware shortcuts for creating pour-over or espresso methods
- A full-height coffee bean editor with a scrollable field area and always-visible save actions on mobile and desktop
- Pour-over and espresso parameters stored directly inside each coffee bean profile
- Bean-to-method shortcuts that open the existing full recipe and temporarily apply the selected bean's parameters
- A dedicated pour-over technique template organized by brew stage; every stage contains start time, cumulative water, action, check, and caution
- Legacy coffee parameter cards remain accessible for data safety, but new coffee parameters are created only inside bean profiles
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

Coffee uses three separate layers so brewing instructions are not duplicated for every bean:

- Coffee bean profile: roaster, origin, variety, process, roast level, roast date, tasting notes, and recommended resting period.
- Bean-owned parameters: pour-over dose, water, grind, temperature and three pour stages; espresso dose, yield, grind, temperature and time.
- Fixed method recipe: one reusable full recipe such as three-stage pour-over or standard espresso extraction. Its parameter card can temporarily display values from the selected coffee bean profile.
- Pour-over method ownership: the bean supplies each stage's time and cumulative water; the technique template supplies the action, check, caution, and follow-along structure.
- Pour-over follow progress is isolated per coffee bean, while edits to stage instructions remain attached to the shared technique template.
- A reusable Espresso technique template for Americanos and milk drinks, with bean-owned dose, yield, grind, temperature, and extraction time.
- Compact coffee technique parameter grids: two columns on mobile and three on desktop, returning to the full table layout while editing.
- Coffee technique pages keep only the selected bean, compact parameters, executable steps, and collapsed troubleshooting; duplicate descriptions, key-state panels, and side notes are removed from the reading flow.
- Coffee technique headers use a compact utility layout for method title, bean switching, archive access, and editing instead of a full recipe hero.
- Coffee bean detail pages consolidate basic data, variety/process rows, flavor, and resting guidance into one scan-friendly profile panel.
- Coffee bean library cards prioritize source, roast level, and flavor for quick selection; record count sits beside the page title and composition details stay in the profile.
- Coffee bean editing separates profile data from brewing parameters with two compact tabs; profile and parameter edit buttons open directly into the relevant tab.
- Mobile navigation uses a compact four-item icon row and removes the repeated sidebar release note so recipe content appears substantially earlier.
- Five-petal yogurt flower bread is included as a complete baking recipe with optimized local photos for windowpane, first proof, final proof, and finished state.
- Generic recipe reading mode prioritizes overview, parameters, executable steps, and collapsed troubleshooting; repeated state galleries and data-management cards remain available only while editing.
- Adding a recipe now opens directly in local note-import mode, with paste or TXT/Markdown loading as the primary path and blank creation retained as a secondary option.
- The temporary combination does not overwrite either the coffee bean profile or the original method recipe.
