import 'package:audioplayers/audioplayers.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const PlayerPage(title: 'Flutter Demo Audio Player Page'),
    );
  }
}

class PlayerPage extends StatefulWidget {
  const PlayerPage({Key? key, required this.title}) : super(key: key);
  final String title;

  @override
  State<PlayerPage> createState() => _PlayerPageState();
}

class _PlayerPageState extends State<PlayerPage> {
  final AudioPlayer _audioPlayer = AudioPlayer();
  bool isPlaying = false;
  String? soundSourceUrl;

  @override
  void initState() {
    super.initState();
    soundSourceUrl = "https://cdn.pozalabs.com/recruit/musics/119.mp3";
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            IconButton(
                icon: Icon(isPlaying ? Icons.pause : Icons.play_arrow),
                onPressed: () {
                  if (_audioPlayer.state == PlayerState.PLAYING) {
                    _audioPlayer.pause();

                    setState(() {
                      isPlaying = false;
                    });
                  } else {
                    if (_audioPlayer.state == PlayerState.PAUSED) {
                      _audioPlayer.resume();
                    } else if (_audioPlayer.state == PlayerState.STOPPED) {
                      _audioPlayer.play(soundSourceUrl!);
                    }

                    setState(() {
                      isPlaying = true;
                    });
                  }
                }),
            IconButton(
                icon: const Icon(Icons.stop),
                onPressed: () {
                  _audioPlayer.stop();

                  setState(() {
                    isPlaying = false;
                  });
                })
          ],
        ),
      ),
    );
  }
}
