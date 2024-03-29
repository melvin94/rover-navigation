class Compass:
    """A `compass` class service that provides the orientation of itself."""

    def __init__(self, orientations: dict[int, str]) -> None:
        """Construct.

        :param orientations: A dictionary of orientations as defined by the
                             user, where the key-value pairs are defined to
                             represent the orientations and the order of those
                             orientations.

                             key: orientation-ordered-index, value: orientation

                             For example:
                             `orientations = {
                                0: 'North'
                                1: 'East',
                                2: 'South',
                                3: 'West'
                             }`

                             Note the following:

                             - The indices must range from [0, N-1], where N is
                             the total number of orientations.

                             - The index order follows a clockwise direction.
                             For example, the orientation indexed as `1` is the
                             next orientation following a clockwise direction
                             from the orientation indexed as `0`.
        """

        self.__orientations = orientations
        self.__orientation_index = None

    def calibrate_compass(self, orientation: str) -> None:
        """Sets the compass orientation from the given orientation. This is
        required before the compass can be used.

        :param orientation: The user-provided starting orientation of the
                            compass.
        """

        # TODO: Refactor for efficiency.
        for orientation_index in self.__orientations:
            if self.__orientations[orientation_index] == orientation:
                self.__orientation_index = orientation_index

    def get_orientation(self) -> str:
        """Gets the compass orientation."""

        return self.__orientations[self.__orientation_index]

    def turn_right(self) -> str:
        """Rotates the compass towards the next clockwise orientation."""

        self.__orientation_index += 1
        if self.__orientation_index >= len(self.__orientations):
            self.__orientation_index = 0

    def turn_left(self) -> str:
        """Rotates the compass towards the next anti-clockwise orientation."""

        self.__orientation_index -= 1
        if self.__orientation_index < 0:
            self.__orientation_index = len(self.__orientations) - 1
