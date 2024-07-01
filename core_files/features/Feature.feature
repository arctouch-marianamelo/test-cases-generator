{Feature}: {Feature}s - screens, bottom sheets, dialogs, etc

# ---------- Screen Reader
Scenario: The device screen reader navigates through the {Feature} {featureType}
    Given the device screen reader is active
        And the app displays the "{Feature}" {featureType}
        And the focus is on the first element available
    When the user starts swiping next to focus on the available elements
    Then the screen reader should focus on each element of the {featureType} following the order and grouping according to Figma annotations

Scenario: The device screen reader reads the {Feature} {featureType} announcements
    Given the device screen reader is active
        And the app displays the "{Feature}" {featureType}
        And the focus is on the first element available
    When the user starts swiping next to focus on the available elements
    Then the screen reader should announce all the elements of the {featureType}
        And the screen reader should announce the elements' labels and types
        And the screen reader should announce the images' alt texts

Scenario: The device screen reader interacts with the {Feature} {featureType} elements
    Given the device screen reader is active
        And the app displays the "{Feature}" {featureType}
    When the screen reader focuses on actionable elements
    Then the screen reader should be able to execute the required action for the element

# ---------- Switch Control
Scenario: The device Switch Control navigates through the {Feature} {featureType}
    Given the device Switch Control is active
        And the app displays the "{Feature}" {featureType}
    When the user navigates through the {featureType}
    Then the Switch Control should focus on all actionable elements on the {featureType} following the order and grouping according to Figma annotations

Scenario: The device Switch Control interacts with the {Feature} {featureType} elements
    Given the device Switch Control is active
        And the app displays the "{Feature}" {featureType}
    When the Switch Control interacts with an actionable element
    Then the app should perform the element related interaction

# ---------- Font Scaling 
Scenario: The app displays the {Feature} {featureType} matching the design prototype when the device is font scaled
    Given the device font is scaled
	    And the app displays the "{Feature}" {featureType}
    Then the app should display the {featureType} matching the design prototype
        And the app should display all the components adapted to fit the {featureType} with the scaled font size

# ---------- Dark Mode
Scenario: The app displays the {Feature} {featureType} matching the design prototype when the device is on the Dark mode
    Given the device is set to Dark mode
	    And the app displays the "{Feature}" {featureType}
    Then the app should display the {featureType} matching the design prototype