Feature: Components - cards, lists, tiles, bottom sheets, etc

# ---------- Screen Reader
Scenario: The device screen reader reads the {Feature} {featureType} {Component} {componentType} announcements
    Given the device screen reader is active    
        And the app displays the "{Feature}" {featureType}
        And the focus is on the "{Component}" {componentType} first element available
    When the user starts swiping next to focus on the available elements
    Then the screen reader should announce all the elements of the {componentType}
        And the screen reader should announce the elements' labels and types
        And the screen reader should announce the images' alt texts

Scenario: The device screen reader navigates through the {Feature} {featureType} {Component} {componentType}
    Given the device screen reader is active
        And the app displays the "{Feature}" {featureType}
        And the focus is on the "{Component}" {componentType} first element available
    When the user starts swiping next to focus on the available elements
    Then the screen reader should focus on each element of the {componentType} following the order and grouping according to Figma annotations

Scenario: The device screen reader interacts with the {Feature} {featureType} {Component} {componentType} elements
    Given the device screen reader is active
        And the app displays the "{Feature}" {featureType}
    When the screen reader focuses on actionable elements in the "{Component}" {componentType}
    Then the screen reader should be able to execute the required action for the element

# ---------- Switch Control
Scenario: The device Switch Control navigates through the {Feature} {featureType} {Component} {componentType}
    Given the device Switch Control is active
        And the app displays the "{Feature}" {featureType}
    When the user navigates through the "{Component}" {componentType}
    Then the Switch Control should focus on all actionable elements on the {componentType} following the order and grouping according to Figma annotations

Scenario: The device Switch Control interacts with the Feature {featureType} {Component} {componentType} elements
    Given the device Switch Control is active
        And the app displays the "{Feature}" {featureType}
    When the Switch Control interacts with an actionable element from the {Component} componentType
    Then the app should perform the element related interaction

# ---------- Font Scaling 
Scenario: The app displays the Feature {featureType} {Component} {componentType} matching the design prototype when the device is font scaled
    Given the device font is scaled
	    And the app displays the "{Feature}" {featureType}
    Then the app should display the "{Component}" {componentType} matching the design prototype
        And the app should display all the components adapted to fit the {componentType} with the scaled font size

# ----------- Dark Mode 
Scenario: The app displays the Feature {featureType} {Component} {componentType} matching the design prototype when the device is on the Dark mode
    Given the device is set to Dark mode    
	    And the app displays the "{Feature}" {featureType}
    Then the app should display the "{Component}" {componentType} matching the design prototype